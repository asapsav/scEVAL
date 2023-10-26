import os
import requests
import tarfile
from tqdm import tqdm

# Determine the script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Create a folder named "downloaded_data" in the script's directory
folder_path = os.path.join(script_dir, "downloaded_data")
os.makedirs(folder_path, exist_ok=True)

# Update the file path to save the file inside the new folder
file_path = os.path.join(folder_path, 'GSE92332.tar')

# Get file size to set up the progress bar
response = requests.head('https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92332&format=file')
total_size = int(response.headers.get('content-length', 0))

# Stream download large file with progress bar
with requests.get('https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92332&format=file', stream=True) as r:
    r.raise_for_status()
    with open(file_path, 'wb') as f, tqdm(
        desc='GSE92332.tar',
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in r.iter_content(chunk_size=1048576):
            f.write(chunk)
            bar.update(len(chunk))

# Unpack large .tar file into the same "downloaded_data" folder
with tarfile.open(file_path, 'r|') as tar:
    tar.extractall(path=folder_path)
