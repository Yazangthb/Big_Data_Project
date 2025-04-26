import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def clean_and_sample_dataset(input_path, output_path, sample_fraction=0.1, random_state=42):
    """
    Clean the dataset and take a stratified sample that maintains the original distribution
    of key columns.
    
    Args:
        input_path (str): Path to the input CSV file
        output_path (str): Path to save the cleaned and sampled CSV
        sample_fraction (float): Fraction of data to sample (default: 0.1)
        random_state (int): Random seed for reproducibility (default: 42)
    """
    
    # Load the dataset
    df = pd.read_csv(input_path)
    
    # Select only the required columns
    required_columns = [
        'id', 'origin', 'destination', 'departure', 'arrival', 
        'duration', 'vehicle_type', 'vehicle_class', 'price', 'fare'
    ]
    
    # Check if all required columns exist
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    df = df[required_columns].copy()
    
    # Clean the data
    # Convert datetime columns to proper format
    df['departure'] = pd.to_datetime(df['departure'], errors='coerce')
    df['arrival'] = pd.to_datetime(df['arrival'], errors='coerce')
    
    # Calculate duration if not properly formatted
    if df['duration'].dtype == 'object':
        df['duration'] = pd.to_timedelta(df['duration']).dt.total_seconds() / 60  # convert to minutes
    
    # Remove rows with missing critical values
    df = df.dropna(subset=['origin', 'destination', 'price', 'vehicle_type'])
    
    # Create bins for stratification to maintain distribution
    # We'll stratify based on origin, destination, vehicle_type, and fare bins
    price_bins = pd.qcut(df['price'], q=10, labels=False, duplicates='drop')
    duration_bins = pd.qcut(df['duration'], q=5, labels=False, duplicates='drop')
    
    # Create a stratification column combining multiple factors
    df['stratify_col'] = (
        df['origin'].astype(str) + "_" + 
        df['destination'].astype(str) + "_" + 
        df['vehicle_type'].astype(str) + "_" + 
        df['fare'].astype(str) + "_" + 
        price_bins.astype(str) + "_" + 
        duration_bins.astype(str)
    )
    
    # Perform stratified sampling
    _, sampled_df = train_test_split(
        df,
        test_size=sample_fraction,
        random_state=random_state,
        stratify=df['stratify_col']
    )
    
    # Drop the temporary stratification column
    sampled_df = sampled_df.drop(columns=['stratify_col'])
    
    # Save the cleaned and sampled dataset
    sampled_df.to_csv(output_path, index=False)
    print(f"Cleaned and sampled dataset saved to {output_path}")
    print(f"Original size: {len(df)}, Sampled size: {len(sampled_df)}")

if __name__ == "__main__":
    input_csv = "data/thegurus-opendata-renfe-trips.csv"  # Adjust if the filename is different
    output_csv = "data/cleaned_sampled_tickets.csv"
    clean_and_sample_dataset(input_csv, output_csv)