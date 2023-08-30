import requests
import yaml
# TODO: add these paths to the function into the config file
with open('src/prepare_GTFS/configs/config.yaml', "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

download_dir = config["raw_data_path"]
api_key = config["api_key"]
bus_feed_link = config["bus_feed_link"]
rail_feed_link = config["rail_feed_link"]
subway_feed_link = config["subway_feed_link"]
commuterbus_feed_link = config["commuterbus_feed_link"]
train_feed_link = config["train_feed_link"]

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

def get_transit_land_url(feed_link, api_key=api_key):
    return f"https://transit.land/api/v2/rest/feed_versions/{feed_link}/download?apikey={api_key}"

if __name__ == "__main__":
    #download_file(get_transit_land_url(bus_feed_link), f"{download_dir}bus.zip")
    download_file(get_transit_land_url(rail_feed_link), f"{download_dir}rail_gtfs.zip")
    download_file(get_transit_land_url(subway_feed_link), f"{download_dir}subway_gtfs.zip")
    download_file(get_transit_land_url(commuterbus_feed_link), f"{download_dir}commuterbus_gtfs.zip")
    download_file(get_transit_land_url(train_feed_link), f"{download_dir}train_gtfs.zip")