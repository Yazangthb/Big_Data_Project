USE team17_projectdb;

DROP TABLE IF EXISTS q6_results;
CREATE EXTERNAL TABLE q6_results (
  ticket_date STRING,
  daily_count BIGINT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q6';

INSERT OVERWRITE TABLE q6_results
SELECT
  FROM_UNIXTIME(CAST(departure / 1000 AS BIGINT), 'yyyy-MM-dd') AS ticket_date,
  COUNT(*) AS daily_count
FROM train_tickets_part
GROUP BY FROM_UNIXTIME(CAST(departure / 1000 AS BIGINT), 'yyyy-MM-dd')
ORDER BY ticket_date;

SELECT * FROM q6_results LIMIT 10;

INSERT OVERWRITE DIRECTORY 'project/output/q6'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM q6_results;
