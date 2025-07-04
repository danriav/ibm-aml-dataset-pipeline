import os
import shutil
import kagglehub

# Download latest version
path = kagglehub.dataset_download("ealtman2019/ibm-transactions-for-anti-money-laundering-aml")

# Define the destination folder within the project
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
tarjet_folder = os.path.join(project_root, 'data', 'raw')

os.makedirs(tarjet_folder, exist_ok=True)

# Copy files from KaggleHub cache to the project data folder
print(f"Copying files from {path} to {tarjet_folder}...")
for filename in os.listdir(path):
    src = os.path.join(path, filename)
    dst = os.path.join(tarjet_folder, filename)
    if os.path.isfile(src):
        shutil.copy2(src, dst)

print("Path to dataset files: ", path)