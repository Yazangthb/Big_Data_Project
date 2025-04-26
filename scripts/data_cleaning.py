import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def clean_dataset(input_path, output_path):
    """
    Clean the dataset and ensure proper data types
    
    Args:
        input_path (str): Path to the input CSV file
        output_path (str): Path to save the cleaned CSV
    """
    
    # Load the dataset
    df = pd.read_csv(input_path)
    
    # Clean the data
    # Convert datetime columns to proper format
    df['departure'] = pd.to_datetime(df['departure'], errors='coerce')
    df['arrival'] = pd.to_datetime(df['arrival'], errors='coerce')
    
    # Fill missing values in vehicle_class with 'Unknown'
    df['vehicle_class'] = df['vehicle_class'].fillna('Unknown')
    
    # Fill missing prices with median price for the same route and vehicle type
    df['price'] = df.groupby(['origin', 'destination', 'vehicle_type'])['price'] \
                   .transform(lambda x: x.fillna(x.median()))
    
    # Calculate duration if not properly formatted or missing
    if df['duration'].isnull().any() or df['duration'].dtype == 'object':
        df['duration'] = (df['arrival'] - df['departure']).dt.total_seconds() / 3600  # convert to hours
    
    # Fill missing fare with 'Standard'
    df['fare'] = df['fare'].fillna('Standard')
    # In data_cleaning.py, add this before saving:
    df['price'] = df['price'].replace('', np.nan)
    df['duration'] = df['duration'].replace('', np.nan)
        # Save the cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to {output_path}")
    print(f"Final size: {len(df)}")
    
if __name__ == "__main__":
    input_csv = "data/sampled_dataset.csv"
    output_csv = "data/cleaned_tickets.csv"
    clean_dataset(input_csv, output_csv)