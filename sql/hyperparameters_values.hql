USE team17_projectdb;

-- Drop if exists
DROP TABLE IF EXISTS model1_hyper;
DROP TABLE IF EXISTS model2_hyper;
DROP TABLE IF EXISTS model3_hyper;
DROP TABLE IF EXISTS model_hyperparameters;

-- Create table for model1
CREATE EXTERNAL TABLE model1_hyper (
  parameter STRING,
  value STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS TEXTFILE
LOCATION 'project/output/model1_best_params'
TBLPROPERTIES ("skip.header.line.count"="1");

-- Create table for model2
CREATE EXTERNAL TABLE model2_hyper (
  parameter STRING,
  value STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS TEXTFILE
LOCATION 'project/output/model2_best_params'
TBLPROPERTIES ("skip.header.line.count"="1");

-- Create table for model3
CREATE EXTERNAL TABLE model3_hyper (
  parameter STRING,
  value STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS TEXTFILE
LOCATION 'project/output/model3_best_params'
TBLPROPERTIES ("skip.header.line.count"="1");

-- Final combined table
CREATE TABLE model_hyperparameters AS
SELECT 'model1' AS model, parameter, value FROM model1_hyper
UNION ALL
SELECT 'model2' AS model, parameter, value FROM model2_hyper
UNION ALL
SELECT 'model3' AS model, parameter, value FROM model3_hyper;

-- Verify
SELECT * FROM model_hyperparameters;

-- Drop models tables, not used
DROP TABLE IF EXISTS model1_hyper;
DROP TABLE IF EXISTS model2_hyper;
DROP TABLE IF EXISTS model3_hyper;

