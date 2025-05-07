USE team17_projectdb;

DROP TABLE IF EXISTS q5_results;
CREATE EXTERNAL TABLE q5_results (
  total_revenue DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q5';

INSERT OVERWRITE TABLE q5_results
SELECT SUM(price) AS total_revenue
FROM train_tickets_part;

SELECT * FROM q5_results;

INSERT OVERWRITE DIRECTORY 'project/output/q5'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM q5_results;
