from pyspark.sql import SparkSession
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark.sql import Row

def trainTree(spark,train_df,test_df):
    

        # Define model
        dt = DecisionTreeRegressor(
            featuresCol="features_simple",
            labelCol="price"
        )

        # Param grid for Decision Tree
        paramGrid_dt = ParamGridBuilder() \
            .addGrid(dt.maxDepth, [3, 5, 7]) \
            .addGrid(dt.minInstancesPerNode, [5, 10, 15]) \
            .build()
        evaluator = RegressionEvaluator(labelCol="price", predictionCol="prediction", metricName="rmse")
        # Cross validation setup
        cv_dt = CrossValidator(estimator=dt,
                             estimatorParamMaps=paramGrid_dt,
                             evaluator=evaluator,
                             numFolds=3,
                             seed=42)

        # Fit model
        cv_model_dt = cv_dt.fit(train_df)
        best_model_dt = cv_model_dt.bestModel

        # Save best model
        best_model_dt.write().overwrite().save(f"hdfs:///user/team17/project/models/model3")

        # Predict and save results
        predictions_dt = best_model_dt.transform(test_df)
        (predictions_dt.select("price", "prediction")
         .coalesce(1)
         .write.mode("overwrite")
         .format("csv")
         .option("header", "true")
         .save(f"hdfs:///user/team17/project/output/model3_predictions"))

        # Evaluate
        # Calculate both metrics
        rmse_evaluator = RegressionEvaluator(labelCol="price", predictionCol="prediction", metricName="rmse")
        r2_evaluator = RegressionEvaluator(labelCol="price", predictionCol="prediction", metricName="r2")

        rmse = rmse_evaluator.evaluate(predictions_dt)
        r2 = r2_evaluator.evaluate(predictions_dt)

        # Create metrics DataFrame with both metrics
        metrics_data = [
            Row(model="model3", metric="RMSE", value=float(rmse)),
            Row(model="model3", metric="R2", value=float(r2))
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
         .save(f"hdfs:///user/team17/project/output/model3_metrics"))

        print(f"Linear Regression (Standard) RMSE: {rmse:.4f}, R²: {r2:.4f}")

