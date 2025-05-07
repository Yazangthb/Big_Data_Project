USE team17_projectdb;

DROP TABLE IF EXISTS q11_results;
CREATE EXTERNAL TABLE q11_results (
  day_of_week STRING,
  ticket_count BIGINT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q11';

INSERT OVERWRITE TABLE q11_results
SELECT
  CASE
    WHEN day = 1 THEN 'Monday'
    WHEN day = 2 THEN 'Tuesday'
    WHEN day = 3 THEN 'Wednesday'
    WHEN day = 4 THEN 'Thursday'
    WHEN day = 5 THEN 'Friday'
    WHEN day = 6 THEN 'Saturday'
    WHEN day = 7 THEN 'Sunday'
  END AS day_of_week,
  COUNT(*) AS ticket_count
FROM (
  SELECT
    CAST(FROM_UNIXTIME(CAST(departure / 1000 AS BIGINT), 'u') AS INT) AS day
  FROM train_tickets_part
) t
GROUP BY day
ORDER BY day;

SELECT * FROM q11_results;

INSERT OVERWRITE DIRECTORY 'project/output/q11'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM q11_results;
