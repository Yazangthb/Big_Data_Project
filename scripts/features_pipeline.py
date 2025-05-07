from pyspark.ml.tuning import CrossValidator
from pyspark.sql import functions as F
from pyspark.sql.types import TimestampType
from pyspark.ml.feature import (StringIndexer, OneHotEncoder, 
                               VectorAssembler, StandardScaler,
                               PolynomialExpansion)
from pyspark.ml import Pipeline

class DataCreator :
    def __init__(self,spark , categoricalCols=None , numericalCols=None):
        self.spark=spark
        self.categoricalCols = categoricalCols if categoricalCols else  ['origin', 'destination', 'vehicle_type', 'vehicle_class' , 'fare']
        self.numericalCols =  numericalCols if numericalCols else ['trip_hours', 'departure_hour', 'departure_day_of_week']
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
        tickets = tickets.withColumn("arrival_time", F.from_unixtime(F.col("arrival")/1000).cast(TimestampType()))

        # Extract useful time features
        tickets = tickets.withColumn("departure_hour", F.hour("departure_time"))
        tickets = tickets.withColumn("departure_day_of_week", F.dayofweek("departure_time"))
        tickets = tickets.withColumn("is_weekend", F.when(F.dayofweek("departure_time").isin([1,7]), 1).otherwise(0))
        tickets = tickets.withColumn("trip_hours", F.col("duration"))

        # Define features and label
        features = [
            'origin', 'destination', 
            'trip_hours', 'vehicle_type', 'vehicle_class',
            'departure_hour', 'departure_day_of_week',  'fare'
        ]
        label = 'price'

        # Clean data
        self.tickets = tickets.select(features + [label]).na.drop()
    def create_pipeline(self):
        indexers = [StringIndexer(inputCol=c, outputCol=f"{c}_index", handleInvalid="keep") 
            for c in self.categoricalCols]

        # 2. Create different pipeline branches
        # --- Branch 1: Simple (indexers + numerical) ---
        simple_assembler = VectorAssembler(
            inputCols=[f"{c}_index" for c in self.categoricalCols] + self.numericalCols,
            outputCol="features_simple"
        )

        # --- Branch 2: Standard (indexers + one-hot + scaled numerical) ---
        encoders = [OneHotEncoder(inputCol=f"{c}_index", outputCol=f"{c}_encoded") 
                   for c in self.categoricalCols]

        numerical_assembler = VectorAssembler(inputCols=self.numericalCols, outputCol="numerical_features")
        scaler = StandardScaler(inputCol="numerical_features", outputCol="scaled_numerical")

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
            simple_assembler,
            *encoders,
            numerical_assembler,
            scaler,
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
        
    