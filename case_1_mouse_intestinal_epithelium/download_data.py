import requests
import tarfile
from tqdm import tqdm

# Get file size to set up the progress bar
response = requests.head('https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92332&format=file')
total_size = int(response.headers.get('content-length', 0))

# Stream download large file with progress bar
with requests.get('https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92332&format=file', stream=True) as r:
    r.raise_for_status()
    with open('GSE92332.tar', 'wb') as f, tqdm(
        desc='GSE92332.tar',
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
            bar.update(len(chunk))

# Unpack large .tar file
#with tarfile.open('GSE92332.tar', 'r|') as tar:
#    tar.extractall()
