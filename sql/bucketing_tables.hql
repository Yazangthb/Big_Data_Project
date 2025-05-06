!set silent false;
!set outputformat table

-- Enable bucketing
SET hive.enforce.bucketing = true;
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;

-- Use your database
USE team17_projectdb;

-- 1) Create the bucketed external table in your own warehouse area
CREATE EXTERNAL TABLE IF NOT EXISTS train_tickets_bucketed (
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
CLUSTERED BY (id) INTO 32 BUCKETS
STORED AS PARQUET
LOCATION 'project/warehouse/train_tickets_bucketed'
TBLPROPERTIES ('parquet.compression'='SNAPPY');

-- 2) Populate it
INSERT OVERWRITE TABLE train_tickets_bucketed
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
FROM TrainTickets;

-- 3) Simple test to confirm it's working
SELECT id, origin, destination FROM train_tickets_bucketed LIMIT 10;
