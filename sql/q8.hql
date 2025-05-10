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

-- Insert first 10 rows into the sample table with corrected column order
INSERT OVERWRITE TABLE dataset_sample
SELECT
  id,
  origin,
  destination,
  departure,
  arrival,
  duration,
  vehicle_type,
  vehicle_class,
  price,
  fare
FROM train_tickets_part
LIMIT 10;
