import os
import datetime
from src.util import config
from travel_time_computation import compute_travel_time_matrices

config = config.get_config()

raw_data_path = config['raw_data_path']
block_group_shapefile_path = raw_data_path + config['block_group_shapefile_path']
md_rac_path = raw_data_path + config['rac_file_path']
md_wac_path = raw_data_path +  + config['wac_file_path']
osm_path = raw_data_path + config['osm_path']
# Filepath to GTFS data
date = "2023-03-06"
departure_time = datetime.datetime(2023, 3, 6, 8, 30)
GTFS = [f"processed_data/updated_gtfs/{date}.zip", 
        'raw_data/rail_gtfs.zip', 
        'raw_data/subway_gtfs.zip',
        'raw_data/commuterbus_gtfs.zip', 
        'raw_data/train_gtfs.zip'
        ]
# Filepath to newline GTFS data
redline = "processed_data/redline.zip"

wait_minutes = 30

from prepare_data import prepare_data_Baltimore

md_rac_df, md_wac_df = prepare_data_Baltimore(block_group_shapefile_path, md_rac_path, md_wac_path)

matrix_before_redline, matrix_after_redline = \
    compute_travel_time_matrices(md_rac_df, md_wac_df, departure_time, osm_path, GTFS, redline, wait_minutes=wait_minutes)

os.makedirs('processed_data/travel_time_matrices', exist_ok=True)
matrix_before_redline.to_csv(f"processed_data/travel_time_matrices/{date}_before_redline.csv", index = False)
matrix_after_redline.to_csv(f"processed_data/travel_time_matrices/{date}_after_redline.csv", index = False)

travel_time = matrix_before_redline.merge(matrix_after_redline, on=['from_id', 'to_id'], suffixes=('_before', '_after'))

travel_time.to_csv(f"processed_data/travel_time_matrices/{date}_travel_time.csv", index = False)
