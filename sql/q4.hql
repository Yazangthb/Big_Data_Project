USE team17_projectdb;

DROP TABLE IF EXISTS q4_results;
CREATE EXTERNAL TABLE q4_results (
  vehicle_class STRING,
  avg_price DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q4';

INSERT OVERWRITE TABLE q4_results
SELECT vehicle_class, AVG(price) AS avg_price
FROM traintickets
GROUP BY vehicle_class
ORDER BY avg_price DESC;

SELECT * FROM q4_results;

INSERT OVERWRITE DIRECTORY 'project/output/q4'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM q4_results;
