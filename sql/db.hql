-- Drop database if exists
DROP DATABASE IF EXISTS team17_projectdb CASCADE;

-- Create the database
CREATE DATABASE team17_projectdb LOCATION 'project/hive/warehouse';

-- Use the database
USE team17_projectdb;

-- Create external table
CREATE EXTERNAL TABLE TrainTickets 
STORED AS AVRO 
LOCATION 'project/warehouse/train_tickets'
TBLPROPERTIES ('avro.schema.url'='project/warehouse/avsc/train_tickets.avsc');

-- Just to check if tables are working
SELECT * FROM TrainTickets LIMIT 10;

