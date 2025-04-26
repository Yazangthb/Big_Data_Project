-- Optional
-- but it is useful if you want to not commit the change when some errors happened before the commit statement
START TRANSACTION;

DROP TABLE IF EXISTS train_tickets CASCADE;

-- Create train_tickets table
CREATE TABLE IF NOT EXISTS train_tickets (
id integer NOT NULL PRIMARY KEY,
origin VARCHAR(50) NOT NULL,
destination VARCHAR(50) NOT NULL,
departure TIMESTAMP NOT NULL,
arrival TIMESTAMP NOT NULL,
duration DECIMAL(10, 2),
vehicle_type VARCHAR(50),
vehicle_class VARCHAR(50),
price DECIMAL(10, 2),
fare VARCHAR(50)
);

-- This is related to how the date types are stored in my dataset
ALTER DATABASE team17_projectdb SET datestyle TO iso, ymd;

COMMIT;