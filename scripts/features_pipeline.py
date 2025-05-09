from pyspark.ml.tuning import CrossValidator
from pyspark.sql import functions as F
from pyspark.sql.types import TimestampType
from pyspark.ml.feature import (StringIndexer, OneHotEncoder, 
                               VectorAssembler, StandardScaler,
                               PolynomialExpansion)
from pyspark import keyword_only
from pyspark.ml.util import DefaultParamsReadable, DefaultParamsWritable
from pyspark.ml import Transformer
from pyspark.sql.functions import from_unixtime, year
from pyspark.ml.param.shared import HasInputCol, HasOutputCols, Param, Params, TypeConverters
from pyspark.ml import Pipeline
import math
class CyclicalEncoder(Transformer, HasInputCol, HasOutputCols, DefaultParamsReadable, DefaultParamsWritable):
    """
    Custom transformer to encode cyclical features using sine/cosine transformation
    """
    @keyword_only
    def __init__(self, inputCol=None, outputCols=None, cycle_length=None):
        super(CyclicalEncoder, self).__init__()
        self.cycle_length = Param(self, "cycle_length", "Length of the cycle")
        self._setDefault(cycle_length=None, outputCols=None)
        kwargs = self._input_kwargs
        self.setParams(**kwargs)
    
    @keyword_only
    def setParams(self, inputCol=None, outputCols=None, cycle_length=None):
        kwargs = self._input_kwargs
        return self._set(**kwargs)
    
    def getCycleLength(self):
        return self.getOrDefault(self.cycle_length)
    
    def _transform(self, df):
        input_col = self.getInputCol()
        output_cols = self.getOutputCols() or [f"{input_col}_sin", f"{input_col}_cos"]
        cycle_length = self.getCycleLength()
        
        if cycle_length is None:
            raise ValueError("cycle_length must be specified")
        
        return (df
                .withColumn(output_cols[0], F.sin(2 * math.pi * F.col(input_col) / cycle_length))
                .withColumn(output_cols[1], F.cos(2 * math.pi * F.col(input_col) / cycle_length))
               )

class TimeDecomposer(Transformer, HasInputCol, HasOutputCols, DefaultParamsReadable, DefaultParamsWritable):
    """
    Custom transformer to decompose a timestamp into its components
    """
    @keyword_only
    def __init__(self, inputCol=None, outputCols=None):
        super(TimeDecomposer, self).__init__()
        kwargs = self._input_kwargs
        self.setParams(**kwargs)
    
    @keyword_only
    def setParams(self, inputCol=None, outputCols=None):
        kwargs = self._input_kwargs
        return self._set(**kwargs)
    
    def _transform(self, df):
        input_col = self.getInputCol()
        output_cols = self.getOutputCols()
        
        return (df
                .withColumn(output_cols[0], F.year(input_col))      # year
                .withColumn(output_cols[1], F.month(input_col))     # month
                .withColumn(output_cols[2], F.dayofmonth(input_col)) # day
                .withColumn(output_cols[3], F.hour(input_col))      # hour
                .withColumn(output_cols[4], F.minute(input_col))    # minute
                .withColumn(output_cols[5], F.second(input_col))    # second
               )

class DataCreator :
    def __init__(self,spark , categoricalCols=None , numericalCols=None):
        self.spark=spark
        self.categoricalCols = categoricalCols if categoricalCols else  ['origin', 'destination', 'vehicle_type', 'vehicle_class' , 'fare']
        self.numericalCols =  numericalCols if numericalCols else ['trip_hours' ]
        self.tickets=None
        self.data_filtering()
        self.full_pipeline= self.create_pipeline()
        self.transformed_data=self.fit_pipeline_and_save()
        
    def data_filtering (self):


        # Load the data
        # tickets = spark.table("train_tickets_part2")

        # Convert UNIX timestamps to human-readable timestamps
        tickets = self.spark.read.format("avro").table('team17_projectdb.train_tickets_part')
        tickets = tickets.withColumn("departure_time", F.from_unixtime(F.col("departure")/1000).cast(TimestampType()))
        # tickets = tickets.withColumn("arrival_time", F.from_unixtime(F.col("arrival")/1000).cast(TimestampType()))

        # Extract useful time features
       
        # tickets = tickets.withColumn("departure_hour", F.hour("departure_time"))
        tickets = tickets.withColumn("departure_day_of_week", F.dayofweek("departure_time"))
        # tickets = tickets.withColumn("is_weekend", F.when(F.dayofweek("departure_time").isin([1,7]), 1).otherwise(0))
        tickets = tickets.withColumn("trip_hours", F.col("duration"))
    
        
        features = [
            'origin', 'destination', 'departure' , 
            'trip_hours', 'vehicle_type', 'vehicle_class',
            'fare'
        ]
        label = 'price'
         # Clean data
        self.tickets = tickets.na.drop()
        
    def create_pipeline(self):
        departure_time_decomposer = TimeDecomposer(inputCol="departure_time", 
                                          outputCols=["dep_year", "dep_month", "dep_day", 
                                                     "dep_hour", "dep_min", "dep_sec"])
        indexers = [StringIndexer(inputCol=c, outputCol=f"{c}_index", handleInvalid="keep") 
            for c in self.categoricalCols]

        # 2. Create different pipeline branches
        # --- Branch 1: Simple (indexers + numerical) ---
        month_encoder = CyclicalEncoder(inputCol="dep_month", outputCols=["month_sin", "month_cos"], cycle_length=12)
        day_encoder = CyclicalEncoder(inputCol="dep_day", outputCols=["day_sin", "day_cos"], cycle_length=31)  
        hour_encoder = CyclicalEncoder(inputCol="dep_hour", outputCols=["hour_sin", "hour_cos"], cycle_length=24)
        minute_encoder = CyclicalEncoder(inputCol="dep_min", outputCols=["min_sin", "min_cos"], cycle_length=60)
        second_encoder = CyclicalEncoder(inputCol="dep_sec", outputCols=["sec_sin", "sec_cos"], cycle_length=60)
        day_of_week_encoder = CyclicalEncoder(inputCol="departure_day_of_week", outputCols=["dow_sin", "dow_cos"], cycle_length=7)
        numericalCols = self.numericalCols + ["dep_year"] + \
            ["month_sin", "month_cos", "day_sin", "day_cos", 
             "hour_sin", "hour_cos", "min_sin", "min_cos", 
             "sec_sin", "sec_cos", "dow_sin", "dow_cos"]

        

        # --- Branch 2: Standard (indexers + one-hot + scaled numerical) ---
        encoders = [OneHotEncoder(inputCol=f"{c}_index", outputCol=f"{c}_encoded") 
                   for c in self.categoricalCols]
        
        numerical_assembler = VectorAssembler(inputCols=self.numericalCols, outputCol="numerical_features")
        scaler = StandardScaler(inputCol="numerical_features", outputCol="scaled_numerical")
        simple_assembler = VectorAssembler(
            inputCols=[f"{c}_index" for c in self.categoricalCols] + ["scaled_numerical"],
            outputCol="features_simple"
        )
        standard_assembler = VectorAssembler(
            inputCols=[f"{c}_encoded" for c in self.categoricalCols] + ["scaled_numerical"],
            outputCol="features_standard"
        )
        
        # --- Branch 3: Polynomial (standard + polynomial expansion) ---
        poly_expansion = PolynomialExpansion(degree=2, inputCol="scaled_numerical", outputCol="poly_features")
        poly_assembler = VectorAssembler(
            inputCols=[f"{c}_encoded" for c in self.categoricalCols] + ["poly_features"],
            outputCol="features_poly"
        )

        # 3. Final unified pipeline
        full_pipeline = Pipeline(stages=indexers + [
            departure_time_decomposer,
            month_encoder,
            day_encoder,
            hour_encoder,
            minute_encoder,
            second_encoder,
            day_of_week_encoder,
            
            *encoders,
            numerical_assembler,
            scaler,
            simple_assembler,
            standard_assembler,
            poly_expansion,
            poly_assembler
        ])
        return full_pipeline
    def fit_pipeline_and_save(self):
        columns_to_keep = [
            "features_standard",  # For standard model
            "features_poly",      # For polynomial model
            "features_simple",    # For decision tree
            "price"              # Target variable
        ]
        train_data, test_data = self.tickets.randomSplit([0.7, 0.3], seed=42)

        pipeline_model = self.full_pipeline.fit(train_data)
        multi_transformed_train = pipeline_model.transform(train_data)
        multi_transformed_test = pipeline_model.transform(test_data)
        multi_transformed_train = multi_transformed_train.select(columns_to_keep)
        multi_transformed_test = multi_transformed_test.select(columns_to_keep)
        # Define HDFS paths
        hdfs_train_path = f"hdfs:///user/team17/project/data/train"
        hdfs_test_path = f"hdfs:///user/team17/project/data/test"
        # Save as JSON files
        (multi_transformed_train.write.mode("overwrite")
                   .format("json")
                   .save(hdfs_train_path))

        (multi_transformed_test.write.mode("overwrite")
                  .format("json")
                  .save(hdfs_test_path))

        # Verify write operations
        def verify_hdfs_path(path):
            try:
                files = self.spark.sparkContext.textFile(path).take(1)
                if files:
                    print(f"Success: Data exists at {path}")
                    return True
                else:
                    print(f"Warning: Empty directory at {path}")
                    return False
            except Exception as e:
                print(f"Error accessing {path}: {str(e)}")
                return False

        print("\nVerification Results:")
        verify_hdfs_path(hdfs_train_path)
        verify_hdfs_path(hdfs_test_path)
        return (multi_transformed_train, multi_transformed_test)
        
    