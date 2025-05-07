USE team17_projectdb;

DROP TABLE IF EXISTS model_evaluation;

CREATE EXTERNAL TABLE model_evaluation (
  model STRING,
  metric STRING,
  value DOUBLE
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS TEXTFILE
LOCATION 'project/output/evaluation'
TBLPROPERTIES (
  "skip.header.line.count"="1"
);

SELECT * FROM model_evaluation;
