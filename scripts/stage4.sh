#!/bin/bash

# Fail immediately if any command fails
set -e

# Print each command for debugging
set -x

# Navigate to project root directory
cd "$(dirname "$0")/.."
BEELINE_CMD="beeline -u jdbc:hive2://hadoop-03.uni.innopolis.ru:10001 -n team17 -p hgVwomtl0OIAe7cF"

# Step 1: create predections table
$BEELINE_CMD -f sql/create_lr_predictions.hql

# Step 2: create evaluation metrics table
$BEELINE_CMD -f sql/model_evaluation_metrics.hql

# Step 3: create hyperparameters table
$BEELINE_CMD -f sql/hyperparameters_values.hql

echo "Stage 4 completed successfully."
