from pyspark.sql import SparkSession
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.regression import LinearRegression
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

def trainPoly(spark,train_df,test_df):
    


    # Define model
           # Define model
        lr_poly = LinearRegression(
            featuresCol="features_poly",
            labelCol="price"
        )

        # Param grid for polynomial LR
        paramGrid_lr_poly = ParamGridBuilder() \
            .addGrid(lr_poly.regParam, [0.01, 0.1, 0.3]) \
            .addGrid(lr_poly.elasticNetParam, [0.0, 0.5, 1.0]) \
            .build()
        evaluator = RegressionEvaluator(labelCol="price", predictionCol="prediction", metricName="rmse")
        # Cross validation setup
        cv_lr_poly = CrossValidator(estimator=lr_poly,
                                 estimatorParamMaps=paramGrid_lr_poly,
                                 evaluator=evaluator,
                                 numFolds=3,
                                 seed=42)

        # Fit model
        cv_model_lr_poly = cv_lr_poly.fit(train_df)
        best_model_lr_poly = cv_model_lr_poly.bestModel

        # Save best model
        best_model_lr_poly.write().overwrite().save(f"hdfs:///user/team17/project/models/model2")

        # Predict and save results
        predictions_lr_poly = best_model_lr_poly.transform(test_df)
        (predictions_lr_poly.select("price", "prediction")
         .coalesce(1)
         .write.mode("overwrite")
         .format("csv")
         .option("header", "true")
         .save(f"hdfs:///user/team17/project/output/model2_predictions"))

        # Evaluate
        

        # 2. Save metrics as CSV
        # Calculate both metrics
        rmse_evaluator = RegressionEvaluator(labelCol="price", predictionCol="prediction", metricName="rmse")
        r2_evaluator = RegressionEvaluator(labelCol="price", predictionCol="prediction", metricName="r2")

        rmse = rmse_evaluator.evaluate(predictions_lr_poly)
        r2 = r2_evaluator.evaluate(predictions_lr_poly)

        # Create metrics DataFrame with both metrics
        metrics_data = [
            Row(model="model2", metric="RMSE", value=float(rmse)),
            Row(model="model2", metric="R2", value=float(r2))
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
         .save(f"hdfs:///user/team17/project/output/model2_metrics"))

        print(f"Linear Regression (Standard) RMSE: {rmse:.4f}, R²: {r2:.4f}")
        
       
        best_params = {
            "elasticNetParam": float(best_model_lr_poly._java_obj.getElasticNetParam()),
            "regParam": float(best_model_lr_poly._java_obj.getRegParam())
        }
        params_rows = [Row(parameter=k, value=v) for k, v in best_params.items()]

        # Define schema
        params_schema = StructType([
            StructField("parameter", StringType(), True),
            StructField("value", DoubleType(), True)
        ])

        # Create DataFrame
        params_df = spark.createDataFrame(params_rows, schema=params_schema)
        params_output_path = "hdfs:///user/team17/project/output/model2_best_params"

        (params_df.coalesce(1)  # Ensure single output file
         .write.mode("overwrite")
         .format("csv")
         .option("header", "true")
         .save(params_output_path))

