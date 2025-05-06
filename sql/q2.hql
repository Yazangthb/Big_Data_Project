USE team17_projectdb;

DROP TABLE IF EXISTS q2_results;
CREATE EXTERNAL TABLE q2_results (
  `date` STRING,
  avg_price DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q2';

INSERT OVERWRITE TABLE q2_results
SELECT
  FROM_UNIXTIME(CAST(departure / 1000 AS BIGINT), 'yyyy-MM-dd') AS `date`,
  AVG(price) AS avg_price
FROM traintickets
GROUP BY FROM_UNIXTIME(CAST(departure / 1000 AS BIGINT), 'yyyy-MM-dd')
ORDER BY `date`;

SELECT * FROM q2_results;

INSERT OVERWRITE DIRECTORY 'project/output/q2'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM q2_results;
