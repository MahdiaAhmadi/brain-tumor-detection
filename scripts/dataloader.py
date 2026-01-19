
import os
import zipfile  
from pathlib import Path
import shutil


def download_brain_tumor_dataset():
    """
    Download Brain Tumor Classification MRI Dataset
    Dataset: https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri
    
    Contains:
    - Training: 2870 images
    - Testing: 394 images
    - Classes: glioma, meningioma, notumor, pituitary
    """
    
    # Create data directory
    data_dir = Path('data/raw')
    data_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if dataset already exists
    expected_dirs = ['Training', 'Testing']
    all_exist = all((data_dir / d).exists() and (data_dir / d).is_dir() for d in expected_dirs)
    
    if all_exist:
        print("\nDataset already exists! Skipping download.")
        print("\n[3/3] Verifying dataset structure...")
        for ed in expected_dirs:
            dir_path = data_dir / ed
            print(f"   ✓ Found: {dir_path}")
        print("Dataset structure verified!")
        return True
    
    zip_path = data_dir / 'brain-tumor-classification-mri.zip'
    
    # Check if zip file already exists
    if zip_path.exists():
        print("\nZip file already exists! Skipping download.")
        print(f"   Using existing: {zip_path}")
    else:
        print("\n[1/3] Downloading dataset from Kaggle...")
       
        # Download using Kaggle API (creates a zip file)
        download_cmd = 'kaggle datasets download -d sartajbhuvaji/brain-tumor-classification-mri -p data/raw/'
        result = os.system(download_cmd)
        
        if result != 0:
            print("\nKaggle download command failed!")
            return False
    
    print("\n[2/3] Extracting files...")
    zip_path = data_dir / 'brain-tumor-classification-mri.zip'
    
    if not zip_path.exists():
        print(f"Zip file not found at: {zip_path}")
        print("\nContents of data/raw/:")
        for item in data_dir.iterdir():
            print(f"   - {item.name}")
        return False
    
    try:
        print(f"Extracting {zip_path.name}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Get list of files to show progress
            files = zip_ref.namelist()
            print(f"   Found {len(files)} files in archive")
            
            # Extract all
            zip_ref.extractall(data_dir)
        
        print("Extraction complete!")
        
        # Clean up zip file
        zip_path.unlink()
        print("Cleaned up zip file")
        
    except Exception as e:
        print(f"Error during extraction: {e}")
        return False
    
    print("\n[3/3] Verifying dataset structure...")
    
    for ed in expected_dirs:
        dir_path = data_dir / ed
        if not dir_path.exists() or not dir_path.is_dir():
            print(f"Error: Expected directory missing: {dir_path}")
            return False
        print(f"   ✓ Found: {dir_path}")
    print("Dataset structure verified!")
    
    return True

if __name__ == "__main__":
    success = download_brain_tumor_dataset()
    if success:
        print("\nDataset downloaded and prepared successfully!")
    else:
        print("\nDataset preparation failed.")