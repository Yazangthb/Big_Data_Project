-- Step 1: Raw table already created
USE team17_projectdb;

DROP TABLE IF EXISTS lr_standard_predictions_raw;

CREATE EXTERNAL TABLE lr_standard_predictions_raw (
  price DOUBLE,
  prediction DOUBLE
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS TEXTFILE
LOCATION 'project/output/lr_standard_predictions'
TBLPROPERTIES (
  "skip.header.line.count"="1"
);

-- Step 2: Final table with one row per price
DROP TABLE IF EXISTS lr_standard_predictions;

CREATE TABLE lr_standard_predictions AS
SELECT price, MIN(prediction) AS prediction
FROM lr_standard_predictions_raw
GROUP BY price;

-- Optional: Drop raw table to save space
DROP TABLE IF EXISTS lr_standard_predictions_raw;
