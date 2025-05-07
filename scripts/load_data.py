from pyspark.sql import SparkSession
from features_pipeline import DataCreator
from run_models import train
from combine import combine_metrics
def main():
    # Initialize Spark
    team = "team17"
    warehouse = "/user/team17/project/warehouse"
    
    # Initialize ONE Spark session for all models
    spark = SparkSession.builder\
        .appName("{} - spark ML".format(team))\
        .master("yarn")\
        .config("hive.metastore.uris", "thrift://hadoop-02.uni.innopolis.ru:9883")\
        .config("spark.sql.warehouse.dir", warehouse)\
        .config("spark.sql.avro.compression.codec", "snappy")\
        .enableHiveSupport()\
        .getOrCreate()
    
    try:
        
        # Create and run the pipeline
        print("Starting data pipeline...")
        data_creator = DataCreator(spark)
        
        print("Pipeline executed successfully!")
        # train_df = spark.read.json("hdfs:///user/team17/project/data/train")
        # test_df = spark.read.json("hdfs:///user/team17/project/data/test")
        train_df,test_df = data_creator.transformed_data
        print("import data sucuess")
        train(spark , train_df,test_df)
        combine_metrics(spark)
    except Exception as e:
        print(f"Pipeline failed: {str(e)}")
        raise
    finally:
        spark.stop()

if __name__ == "__main__":
    main()