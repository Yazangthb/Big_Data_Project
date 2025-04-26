#!/bin/bash

# Install Kaggle API if not already installed
pip install kaggle

# Set up Kaggle API credentials (assuming you have your kaggle.json file ready)
mkdir -p ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Download the dataset
kaggle datasets download -d thegurusteam/spanish-high-speed-rail-system-ticket-pricing

# Unzip the dataset
unzip spanish-high-speed-rail-system-ticket-pricing.zip -d data

echo "Dataset downloaded and extracted to data/ directory"