#!/bin/bash

# Fail immediately if any command fails
set -e

# Print each command for debugging
set -x

# Navigate to project root directory
cd "$(dirname "$0")/.."

# Beeline connection string
BEELINE_CMD="beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team17 -p hgVwomtl0OIAe7cF"

# Step 1: Create partitioned & bucketed table
$BEELINE_CMD -f sql/partition_bucketing_table.hql

# Step 2: Run queries q1.hql to q10.hql
for i in {1..12}; do
    $BEELINE_CMD -f sql/q${i}.hql
done

echo "Stage 2 completed successfully."
