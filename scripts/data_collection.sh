#!/bin/bash
# Export your Kaggle username and API key
# export KAGGLE_USERNAME=<YOUR USERNAME>
# export KAGGLE_KEY=<YOUR KAGGLE KEY>

# Download the dataset
curl -L -u yazanalnakri:92aedf09a13e123a22205dedfc0f2305\
  -o trains-yazan.zip\
  https://www.kaggle.com/api/v1/datasets/download/yazanalnakri/trains-yazan

# Check if the download was successful
if [ $? -eq 0 ]; then
    echo "Download successful. Unzipping the file..."
    
    # Unzip the file
    unzip trains-yazan.zip -d trains-yazan
    
    # Check if unzip was successful
    if [ $? -eq 0 ]; then
        echo "Unzipping completed successfully."
        
        # Create data directory if it doesn't exist
        mkdir -p data
        
        # Move the specific file to the data directory
        if [ -f "trains-yazan/half_sampled_dataset.csv" ]; then
            mv trains-yazan/half_sampled_dataset.csv data/half_sampled_dataset.csv
            echo "File moved to data/half_sampled_dataset.csv"
            
            # Optional: Remove the trains-yazan directory after moving the file
            # rm -r trains-yazan
            # echo "Removed trains-yazan directory"
        else
            echo "Error: half_sampled_dataset.csv not found in trains-yazan directory"
            exit 1
        fi
        
        # Optional: Remove the zip file after extraction
        # rm trains-yazan.zip
        # echo "Zip file removed."
    else
        echo "Error occurred while unzipping the file."
        exit 1
    fi
else
    echo "Error occurred during download."
    exit 1
fi