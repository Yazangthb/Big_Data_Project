#!/bin/bash

# Set environment
export HADOOP_CONF_DIR=/etc/hadoop/conf
export YARN_CONF_DIR=/etc/hadoop/conf
export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=python3

# Run the pipeline
spark-submit \
  --master yarn \
  --num-executors 2 \
  --executor-memory 2G \
  load_data.py

# Check status
if [ $? -eq 0 ]; then
    echo "Pipeline completed successfully"
else
    echo "Pipeline failed" >&2
    exit 1
fi

