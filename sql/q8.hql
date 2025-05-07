USE team17_projectdb;

-- Drop existing sample table if it exists
DROP TABLE IF EXISTS dataset_sample;

-- Create external table for sample data
CREATE EXTERNAL TABLE dataset_sample (
  id BIGINT,
  origin STRING,
  destination STRING,
  departure BIGINT,
  arrival BIGINT,
  duration DOUBLE,
  vehicle_type STRING,
  vehicle_class STRING,
  price DOUBLE,
  fare STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/sample';

-- Insert first 100 rows into the sample table
INSERT OVERWRITE TABLE dataset_sample
SELECT *
FROM train_tickets_part
LIMIT 10;

-- Optional: export the sample as CSV for Superset
INSERT OVERWRITE DIRECTORY 'project/output/sample'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM dataset_sample;
