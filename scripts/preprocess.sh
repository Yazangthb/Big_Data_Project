#!/bin/bash
# Clean the data (optional)
python3 scripts/data_cleaning.py

# Create database tables and import data
python3 scripts/build_projectdb.py

# Verify the data was imported correctly
psql -h hadoop-04.uni.innopolis.ru -p 5432 -U team17 -d team17_projectdb -f sql/test_database.sql