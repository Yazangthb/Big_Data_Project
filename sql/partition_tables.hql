-- Enable dynamic partitioning (nonstrict mode)
SET hive.exec.dynamic.partition=true;
SET hive.exec.dynamic.partition.mode=nonstrict;
SET hive.exec.max.dynamic.partitions=1000;
SET hive.exec.max.dynamic.partitions.pernode=500;
SET hive.optimize.index.filter=true;
SET hive.optimize.ppd=true;

-- Switch to your project database
DROP DATABASE IF EXISTS team17_projectdb CASCADE;
CREATE DATABASE IF NOT EXISTS team17_projectdb LOCATION 'project/hive/warehouse';
USE team17_projectdb;

CREATE EXTERNAL TABLE TrainTickets 
STORED AS AVRO 
LOCATION 'project/warehouse/train_tickets'
TBLPROPERTIES ('avro.schema.url'='project/warehouse/avsc/train_tickets.avsc');

-- 1) Create a partitioned Parquet table for TrainTickets by origin
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
STORED AS PARQUET
LOCATION 'project/warehouse/train_tickets_part'
TBLPROPERTIES ('parquet.compression'='SNAPPY');

-- 2) Load data dynamically into partitions (one statement handles all origins)
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

-- 3) Verify partitions and sample data
SHOW PARTITIONS train_tickets_part;
SELECT * FROM train_tickets_part WHERE origin='MADRID' LIMIT 10;
SELECT origin, COUNT(*) FROM train_tickets_part GROUP BY origin;

-- 4) Create a multi-column partitioned Parquet table by vehicle_type and vehicle_class
CREATE EXTERNAL TABLE IF NOT EXISTS train_tickets_part2 (
  id BIGINT,
  origin STRING,
  destination STRING,
  departure BIGINT,
  arrival BIGINT,
  duration DOUBLE,
  price DOUBLE,
  fare STRING
)
PARTITIONED BY (
  vehicle_type STRING,
  vehicle_class STRING
)
STORED AS PARQUET
LOCATION 'project/warehouse/train_tickets_part2'
TBLPROPERTIES ('parquet.compression'='SNAPPY');

-- 5) Load data dynamically for both vehicle_type and vehicle_class
INSERT OVERWRITE TABLE train_tickets_part2
PARTITION (vehicle_type, vehicle_class)
SELECT
  id,
  origin,
  destination,
  departure,
  arrival,
  duration,
  price,
  fare,
  vehicle_type,
  vehicle_class
FROM TrainTickets;

-- 6) Verify partitions and sample data
SHOW PARTITIONS train_tickets_part2;
SELECT * FROM train_tickets_part2 WHERE vehicle_type='AVE' AND vehicle_class='Turista' LIMIT 10;