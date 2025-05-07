from pyspark.sql import SparkSession
from train_lr import trainLr
from train_polynomial import trainPoly
from train_tree import trainTree

def train(spark,train_df , test_df):
  
    # Load/preprocess data once (reused across models)
    
    # train_df = spark.read.json("hdfs:///user/team17/project/data/train")
    # test_df = spark.read.json("hdfs:///user/team17/project/data/test")

    # Train models sequentially (passing the shared Spark session)
    trainLr(spark, train_df,test_df)
    trainPoly(spark,  train_df,test_df)
    trainTree(spark,  train_df,test_df)
    print("succes")
        
  # Cleanup only after all models finish

