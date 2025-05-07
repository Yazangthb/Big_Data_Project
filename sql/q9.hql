USE team17_projectdb;

-- Drop existing results table if it exists
DROP TABLE IF EXISTS vehicle_type_distribution;

-- Create external table for vehicle_type counts
CREATE EXTERNAL TABLE vehicle_type_distribution (
  vehicle_type STRING,
  ticket_count BIGINT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/vehicle_type_distribution';

-- Insert aggregated data into the table
INSERT OVERWRITE TABLE vehicle_type_distribution
SELECT
  vehicle_type,
  COUNT(*) AS ticket_count
FROM train_tickets_part
GROUP BY vehicle_type;

-- Export to CSV for Superset
INSERT OVERWRITE DIRECTORY 'project/output/vehicle_type_distribution'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM vehicle_type_distribution;
