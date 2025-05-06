USE team17_projectdb;

DROP TABLE IF EXISTS q6_results;
CREATE EXTERNAL TABLE q6_results (
  total_tickets BIGINT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q6';

INSERT OVERWRITE TABLE q6_results
SELECT COUNT(*) AS total_tickets
FROM traintickets;

SELECT * FROM q6_results;

INSERT OVERWRITE DIRECTORY 'project/output/q6'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM q6_results;
