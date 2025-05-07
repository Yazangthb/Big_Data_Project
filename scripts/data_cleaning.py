import pandas as pd
import numpy as np
from collections import defaultdict
from tqdm import tqdm
import os

def compute_medians(input_path):
    """
    Compute median prices for each group in a memory-efficient manner.
    
    Args:
        input_path (str): Path to the input CSV file
        
    Returns:
        pd.DataFrame: DataFrame containing group medians
    """
    # Get total rows for progress bar (approximate)
    total_rows = sum(1 for _ in open(input_path)) - 1  # Subtract header
    
    group_prices = defaultdict(list)
    
    print("Computing price medians (first pass)...")
    
    # Read the CSV in chunks to collect prices per group
    for chunk in tqdm(
        pd.read_csv(
            input_path,
            usecols=['origin', 'destination', 'vehicle_type', 'price'],
            dtype={
                'origin': 'category',
                'destination': 'category',
                'vehicle_type': 'category',
                'price': 'float32'
            },
            chunksize=10000
        ),
        total=total_rows//10000 + 1,
        unit='chunk'
    ):
        # Convert price to numeric and drop rows with NaN prices
        chunk['price'] = pd.to_numeric(chunk['price'], errors='coerce')
        chunk.dropna(subset=['price'], inplace=True)
        
        # Group by origin, destination, vehicle_type and collect prices
        grouped = chunk.groupby(['origin', 'destination', 'vehicle_type'])['price']
        for name, group in grouped:
            group_prices[name].extend(group.tolist())
    
    print("Calculating final medians...")
    # Calculate medians for each group
    medians = []
    for key, prices in tqdm(group_prices.items(), desc="Processing groups"):
        if prices:
            medians.append({
                'origin': key[0],
                'destination': key[1],
                'vehicle_type': key[2],
                'price_median': np.median(prices)
            })
    
    return pd.DataFrame(medians)

def clean_dataset(input_path, output_path, chunksize=10000):
    """
    Clean the dataset in chunks to minimize memory usage.
    
    Args:
        input_path (str): Path to the input CSV file
        output_path (str): Path to save the cleaned CSV
        chunksize (int): Number of rows per processing chunk
    """
    # Get total rows for progress bar (approximate)
    total_rows = sum(1 for _ in open(input_path)) - 1  # Subtract header
    print(total_rows)
    # Step 1: Compute group medians for price imputation
    group_medians = compute_medians(input_path)
    
    # Step 2: Process and clean data in chunks
    print("\nCleaning data (second pass)...")
    
    # Remove output file if it exists
    if os.path.exists(output_path):
        os.remove(output_path)
    
    first_chunk = True
    processed_rows = 0
    
    for chunk in tqdm(
        pd.read_csv(
            input_path,
            chunksize=chunksize,
            dtype={
                'vehicle_class': 'category',
                'origin': 'category',
                'destination': 'category',
                'vehicle_type': 'category',
                'fare': 'category',
                'price': 'float32',
                'duration': 'float32'
            }
        ),
        total=total_rows//chunksize + 1,
        unit='chunk'
    ):
        processed_rows += len(chunk)
        
        # Convert datetime columns
        chunk['departure'] = pd.to_datetime(chunk['departure'], errors='coerce')
        chunk['arrival'] = pd.to_datetime(chunk['arrival'], errors='coerce')
        
        # Handle missing vehicle_class
        chunk['vehicle_class'] = chunk['vehicle_class'].cat.add_categories(['Unknown']).fillna('Unknown')
        
        # Merge with precomputed medians for price imputation
        chunk = chunk.merge(
            group_medians,
            on=['origin', 'destination', 'vehicle_type'],
            how='left'
        )
        chunk['price'] = chunk['price'].fillna(chunk['price_median'])
        chunk.drop(columns=['price_median'], inplace=True)
        
        # Convert and clean duration
        chunk['duration'] = pd.to_numeric(chunk['duration'], errors='coerce')
        duration_mask = chunk['duration'].isna()
        if duration_mask.any():
            chunk.loc[duration_mask, 'duration'] = (
                (chunk['arrival'] - chunk['departure']).dt.total_seconds() / 3600
            )
        chunk['duration'] = chunk['duration'].astype('float32')
        
        # Handle missing fare
        chunk['fare'] = chunk['fare'].cat.add_categories(['Standard']).fillna('Standard')
        
        # Ensure consistent data types
        chunk['vehicle_class'] = chunk['vehicle_class'].astype('category')
        chunk['fare'] = chunk['fare'].astype('category')
        
        # Write cleaned chunk to CSV
        chunk.to_csv(
            output_path,
            mode='a',
            header=first_chunk,
            index=False,
            na_rep='NULL'
        )
        first_chunk = False
    
    print(f"\n Cleaning complete! Processed {processed_rows:,} rows.")
    print(f"Cleaned dataset saved to {output_path}")
    print(f"Final file size: {os.path.getsize(output_path)/1024/1024:.2f} MB")

if __name__ == "__main__":
    input_csv = "data/half_sampled_dataset.csv"
    output_csv = "data/cleaned_tickets.csv"
    clean_dataset(input_csv, output_csv)