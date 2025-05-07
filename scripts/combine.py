from pyspark.sql import SparkSession

def combine_metrics(spark):
    # Read and union all metrics files with a list comprehension
    combined_df = spark.read.csv("hdfs:///user/team17/project/output/model1_metrics", header=True) \
        .union(spark.read.csv("hdfs:///user/team17/project/output/model2_metrics", header=True)) \
        .union(spark.read.csv("hdfs:///user/team17/project/output/model3_metrics", header=True))
    
    # Save the combined results
    combined_df.coalesce(1).write.mode("overwrite").csv(
        "hdfs:///user/team17/project/output/evaluation",
        header=True
    )
    return combined_df

if __name__ == "__main__":
    spark = SparkSession.builder.appName("CombineMetrics").getOrCreate()
    combine_metrics(spark).show()
    spark.stop()