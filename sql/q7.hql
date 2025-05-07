USE team17_projectdb;

DROP TABLE IF EXISTS dataset_description;
CREATE EXTERNAL TABLE dataset_description (
  column_name STRING,
  data_type STRING,
  comment STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LOCATION 'project/hive/warehouse/description';

INSERT OVERWRITE TABLE dataset_description VALUES
('id', 'BIGINT', 'Unique identifier for each train ticket.'),
('origin', 'STRING', 'City or station where the train journey starts.'),
('destination', 'STRING', 'City or station where the train journey ends.'),
('departure', 'BIGINT (epoch ms)', 'Departure timestamp in milliseconds since epoch (UNIX time).'),
('arrival', 'BIGINT (epoch ms)', 'Arrival timestamp in milliseconds since epoch (UNIX time).'),
('duration', 'DOUBLE', 'Duration of the train trip in hours.'),
('vehicle_type', 'STRING', 'Category/type of train used for the journey (e.g., AVE, MD, LD).'),
('vehicle_class', 'STRING', 'Class or comfort level of the ticket (e.g., Turista, Preferente, Turista con enlace).'),
('price', 'DOUBLE', 'Actual price of the ticket in Euros. This is the target variable for regression.'),
('fare', 'STRING', 'Fare plan or promotion type (e.g., Promo, Promo+, Flexible). It reflects pricing strategy.');

INSERT OVERWRITE DIRECTORY 'project/output/description'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM dataset_description;
