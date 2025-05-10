from pyspark.sql import SparkSession
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.regression import LinearRegression
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, StringType, DoubleType


def trainLr(spark,train_df,test_df):
    


    # Define model
    lr_standard = LinearRegression(
        featuresCol="features_standard",
        labelCol="price"
    )

    # Param grid for standard LR
    paramGrid_lr_standard = ParamGridBuilder() \
        .addGrid(lr_standard.regParam, [0.1, 0.3, 0.5]) \
        .addGrid(lr_standard.elasticNetParam, [0.5, 0.8, 1.0]) \
        .build()

    # Cross validation setup
    evaluator = RegressionEvaluator(labelCol="price", predictionCol="prediction", metricName="rmse")
    cv_lr_standard = CrossValidator(estimator=lr_standard,
                                  estimatorParamMaps=paramGrid_lr_standard,
                                  evaluator=evaluator,
                                  numFolds=3,
                                  seed=42)

    # Fit model
    cv_model_lr_standard = cv_lr_standard.fit(train_df)
    best_model_lr_standard = cv_model_lr_standard.bestModel
    # Save best model
    
    best_model_lr_standard.write().overwrite().save(f"hdfs:///user/team17/project/models/model1")
    
    # Predict and save results
    predictions_lr_standard = best_model_lr_standard.transform(test_df)
    (predictions_lr_standard.select("price", "prediction")
     .coalesce(1)
     .write.mode("overwrite")
     .format("csv")
     .option("header", "true")
     .save(f"hdfs:///user/team17/project/output/model1_predictions"))

    # Evaluate
   # Calculate both metrics
    rmse_evaluator = RegressionEvaluator(labelCol="price", predictionCol="prediction", metricName="rmse")
    r2_evaluator = RegressionEvaluator(labelCol="price", predictionCol="prediction", metricName="r2")
    
    rmse = rmse_evaluator.evaluate(predictions_lr_standard)
    r2 = r2_evaluator.evaluate(predictions_lr_standard)

    # Create metrics DataFrame with both metrics
    metrics_data = [
        Row(model="model1", metric="RMSE", value=float(rmse)),
        Row(model="model1", metric="R2", value=float(r2))
    ]
    
    metrics_schema = StructType([
        StructField("model", StringType(), True),
        StructField("metric", StringType(), True),
        StructField("value", DoubleType(), True)
    ])
    
    metrics_df = spark.createDataFrame(metrics_data, schema=metrics_schema)

    # Save metrics
    (metrics_df.coalesce(1)
     .write.mode("overwrite")
     .format("csv")
     .option("header", "true")
     .save(f"hdfs:///user/team17/project/output/model1_metrics"))

    print(f"Linear Regression (Standard) RMSE: {rmse:.4f}, R²: {r2:.4f}")
    best_params = {
    "elasticNetParam": float(best_model_lr_standard._java_obj.getElasticNetParam()),
    "regParam": float(best_model_lr_standard._java_obj.getRegParam())
    }
    params_rows = [Row(parameter=k, value=v) for k, v in best_params.items()]

    # Define schema
    params_schema = StructType([
        StructField("parameter", StringType(), True),
        StructField("value", DoubleType(), True)
    ])

    # Create DataFrame
    params_df = spark.createDataFrame(params_rows, schema=params_schema)
    params_output_path = "hdfs:///user/team17/project/output/model1_best_params"
    
    (params_df.coalesce(1)  # Ensure single output file
     .write.mode("overwrite")
     .format("csv")
     .option("header", "true")
     .save(params_output_path))