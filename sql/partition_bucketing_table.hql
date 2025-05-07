-- Enable dynamic partitioning (nonstrict mode) and bucketing enforcement
SET hive.exec.dynamic.partition=true;
SET hive.exec.dynamic.partition.mode=nonstrict;
SET hive.exec.max.dynamic.partitions=1000;
SET hive.exec.max.dynamic.partitions.pernode=500;
SET hive.optimize.index.filter=true;
SET hive.optimize.ppd=true;

-- Enforce bucketing for INSERT statements
SET hive.enforce.bucketing=true;

-- Switch to your project database
DROP DATABASE IF EXISTS team17_projectdb CASCADE;
CREATE DATABASE IF NOT EXISTS team17_projectdb LOCATION 'project/hive/warehouse';
USE team17_projectdb;

-- Original AVRO table
CREATE EXTERNAL TABLE TrainTickets 
STORED AS AVRO 
LOCATION 'project/warehouse/train_tickets'
TBLPROPERTIES ('avro.schema.url'='project/warehouse/avsc/train_tickets.avsc');

-- 1) Create a partitioned & bucketed Parquet table for TrainTickets by origin, bucketed by destination
CREATE EXTERNAL TABLE IF NOT EXISTS train_tickets_part (
  id BIGINT,
  destination STRING,
  departure BIGINT,
  arrival BIGINT,
  duration DOUBLE,
  vehicle_type STRING,
  vehicle_class STRING,
  price DOUBLE,
  fare STRING
)
PARTITIONED BY (origin STRING)
CLUSTERED BY (ID) INTO 32 BUCKETS
STORED AS PARQUET
LOCATION 'project/warehouse/train_tickets_part'
TBLPROPERTIES (
  'parquet.compression'='SNAPPY',
  'bucketed'='true'
);

-- 2) Load data dynamically into partitions (one statement handles all origins) with bucketing
INSERT OVERWRITE TABLE train_tickets_part
PARTITION (origin)
SELECT
  id,
  destination,
  departure,
  arrival,
  duration,
  vehicle_type,
  vehicle_class,
  price,
  fare,
  origin
FROM TrainTickets;

-- 3) Verify partitions, buckets and sample data
SHOW PARTITIONS train_tickets_part;

-- You can also look at the underlying file layout to see buckets under each origin folder
SELECT * FROM train_tickets_part WHERE origin='MADRID' LIMIT 10;
SELECT origin, COUNT(*) FROM train_tickets_part GROUP BY origin;

-- 4) Drop the old TrainTickets table to free up space
DROP TABLE IF EXISTS TrainTickets;