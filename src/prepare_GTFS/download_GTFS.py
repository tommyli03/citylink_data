import requests

# TODO: add these paths to the function into the config file
download_dir = 'raw_data/'
api_key = 'T2Jljq0EQqqe1JMfijkn3RdtVxoYpwuq'
bus_feed_link = '8523f088e05dcd273b369dd4d65eb771c73c0a22'
rail_feed_link = 'c4233b29806296fc80209881fd9cec6c49fd9380'
subway_feed_link = '9b0a275f899fcb67a9d2107be8b9976326507a35'
commuterbus_feed_link = '6cc96d82827a3dfb39807521ad8a77cf8d77b368'
train_feed_link = '32c1ab0bebce48f0f58a8110ebe245ccb5008930'


def get_transit_land_url(feed_link, api_key=api_key):
    return f"https://transit.land/api/v2/rest/feed_versions/{feed_link}/download?apikey={api_key}"


def download_file(url, local_filename):
    '''
    params:
        url: url of the file to download
        local_filename: local path to save the file. Should end with .zip
    '''
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_filename, "wb") as f:
            f.write(response.content)
        print(f"File {local_filename} downloaded successfully.")
    else:
        print("Failed to download the file.")

if __name__ == "__main__":
    #download_file(get_transit_land_url(bus_feed_link), f"{download_dir}bus.zip")
    download_file(get_transit_land_url(rail_feed_link), f"{download_dir}rail_gtfs.zip")
    download_file(get_transit_land_url(subway_feed_link), f"{download_dir}subway_gtfs.zip")
    download_file(get_transit_land_url(commuterbus_feed_link), f"{download_dir}commuterbus_gtfs.zip")
    download_file(get_transit_land_url(train_feed_link), f"{download_dir}train_gtfs.zip")