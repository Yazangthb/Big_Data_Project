USE team17_projectdb;

DROP TABLE IF EXISTS q1_results;
CREATE EXTERNAL TABLE q1_results (
  origin STRING,
  ticket_count INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q1';

INSERT OVERWRITE TABLE q1_results
SELECT
  origin,
  COUNT(*) AS ticket_count
FROM traintickets
GROUP BY origin
ORDER BY ticket_count DESC
LIMIT 10;

SELECT * FROM q1_results;

INSERT OVERWRITE DIRECTORY 'project/output/q1'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM q1_results;
