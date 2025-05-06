import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def install_kaggle_dataset(dataset_name, download_path):
    """
    Install a Kaggle dataset
    
    Args:
        dataset_name (str): Dataset identifier in format 'username/dataset-name'
        download_path (str): Path to download and extract the dataset
    """
    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()
    
    # Create download directory if it doesn't exist
    os.makedirs(download_path, exist_ok=True)
    
    # Download dataset
    print(f"Downloading dataset {dataset_name}...")
    api.dataset_download_files(dataset_name, path=download_path, unzip=False)
    
    # Find the downloaded zip file
    zip_file = [f for f in os.listdir(download_path) if f.endswith('.zip')][0]
    zip_path = os.path.join(download_path, zip_file)
    
    # Extract the dataset
    print(f"Extracting {zip_file}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(download_path)
    
    # Remove the zip file
    os.remove(zip_path)
    print("Dataset installed successfully!")

if __name__ == "__main__":
    dataset = "yazanalnakri/trains-yazan"
    install_path = "./trains_dataset"  # Change this to your desired path
    
    install_kaggle_dataset(dataset, install_path)