USE team17_projectdb;

-- Drop previous table
DROP TABLE IF EXISTS q1_results;

-- Create external table with origin and destination counts
CREATE EXTERNAL TABLE q1_results (
  city STRING,
  origin_count INT,
  destination_count INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/q1';

-- Insert combined data
INSERT OVERWRITE TABLE q1_results
SELECT
  COALESCE(o.city, d.city) AS city,
  COALESCE(o.origin_count, 0) AS origin_count,
  COALESCE(d.destination_count, 0) AS destination_count
FROM
  (SELECT origin AS city, COUNT(*) AS origin_count FROM train_tickets_part GROUP BY origin) o
FULL OUTER JOIN
  (SELECT destination AS city, COUNT(*) AS destination_count FROM train_tickets_part GROUP BY destination) d
ON o.city = d.city;

-- Export to output directory for Superset
INSERT OVERWRITE DIRECTORY 'project/output/q1'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM q1_results;
