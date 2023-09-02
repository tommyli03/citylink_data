import yaml
import requests

def get_config():
    with open('src/config.yaml', "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config


def download_file(url, local_filename):
    '''
    params:
        url: url of the file to download
        local_filename: local path to save the file.
    '''
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_filename, "wb") as f:
            f.write(response.content)
        print(f"File {local_filename} downloaded successfully.")
    else:
        print("Failed to download the file.")