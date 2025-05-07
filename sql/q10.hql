USE team17_projectdb;

-- 1) Drop and create correlation_matrix table
DROP TABLE IF EXISTS correlation_matrix;
CREATE EXTERNAL TABLE correlation_matrix (
  feature_x STRING,
  feature_y STRING,
  correlation DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'project/hive/warehouse/correlation';

-- 2) Insert correlations one-by-one to avoid Tez counter limit
--    (Only numerical columns are used: departure, arrival, duration, price)

INSERT INTO correlation_matrix
SELECT 'departure', 'arrival', corr(departure, arrival) FROM train_tickets_part;

INSERT INTO correlation_matrix
SELECT 'departure', 'duration', corr(departure, duration) FROM train_tickets_part;

INSERT INTO correlation_matrix
SELECT 'departure', 'price', corr(departure, price) FROM train_tickets_part;

INSERT INTO correlation_matrix
SELECT 'arrival', 'duration', corr(arrival, duration) FROM train_tickets_part;

INSERT INTO correlation_matrix
SELECT 'arrival', 'price', corr(arrival, price) FROM train_tickets_part;

INSERT INTO correlation_matrix
SELECT 'duration', 'price', corr(duration, price) FROM train_tickets_part;

-- 3) View results
SELECT * FROM correlation_matrix;

-- 4) Export for Superset
INSERT OVERWRITE DIRECTORY 'project/output/correlation'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM correlation_matrix;
