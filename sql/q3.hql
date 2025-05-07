USE team17_projectdb;

DROP TABLE IF EXISTS q3_results;
CREATE EXTERNAL TABLE q3_results (
  fare STRING,
  count INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q3';

INSERT OVERWRITE TABLE q3_results
SELECT fare, COUNT(*) AS count
FROM train_tickets_part
GROUP BY fare
ORDER BY count DESC;

SELECT * FROM q3_results;

INSERT OVERWRITE DIRECTORY 'project/output/q3'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM q3_results;
