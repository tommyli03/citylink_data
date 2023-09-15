import os
from datetime import datetime, timedelta
from src.util import get_config
from travel_time_computation import compute_travel_time_matrices

config = get_config()

raw_data_path = config['raw_data_path']
block_group_shapefile_path = raw_data_path + config['block_group_shapefile_path']
md_rac_path = raw_data_path + config['rac_file_path']
md_wac_path = raw_data_path + config['wac_file_path']
osm_path = raw_data_path + config['osm_path']
# Filepath to GTFS data

begin_date = config['begin_date']
end_date = config['end_date']

# Define the step (in this case, one day)
step = timedelta(days=1)

# Iterate through dates from begin_date to end_date
current_date = begin_date

while current_date <= end_date:

    month = int(current_date.strftime('%m'))
    day = int(current_date.strftime('%d'))
    date = current_date.strftime('%Y-%m-%d')
    current_date += step

    bus_gtfs_path = f'processed_data/updated_gtfs/{date}.zip'
    if os.path.exists(bus_gtfs_path):
        print(date)
        departure_time = datetime(2023, month, day, 8, 0)
        GTFS = [f"processed_data/updated_gtfs/{date}.zip", 
                'raw_data/rail_gtfs.zip', 
                'raw_data/subway_gtfs.zip',
                'raw_data/commuterbus_gtfs.zip', 
                'raw_data/train_gtfs.zip'
                ]
        # Filepath to newline GTFS data
        redline = "processed_data/redline.zip"

        wait_minutes = 10

        from prepare_data import prepare_data_Baltimore

        md_rac_df, md_wac_df = prepare_data_Baltimore(block_group_shapefile_path, md_rac_path, md_wac_path)

        matrix_before_redline, matrix_after_redline = \
            compute_travel_time_matrices(md_rac_df, md_wac_df, departure_time, osm_path, GTFS, redline, wait_minutes=wait_minutes)

        os.makedirs('processed_data/travel_time_matrices', exist_ok=True)
        #matrix_before_redline.to_csv(f"processed_data/travel_time_matrices/{date}_before_redline.csv", index = False)
        #matrix_after_redline.to_csv(f"processed_data/travel_time_matrices/{date}_after_redline.csv", index = False)

        travel_time = matrix_before_redline.merge(matrix_after_redline, on=['from_id', 'to_id'], suffixes=('_before', '_after'))

        # filter out rows where travel time after is nan
        travel_time = travel_time[~travel_time['travel_time_after'].isna()]
        # filter out rows where travel time, both before or after, are greater than 90 minutes
        travel_time = travel_time[(travel_time['travel_time_before'] <= 90) | (travel_time['travel_time_after'] <= 90)]
        travel_time.to_csv(f"processed_data/travel_time_matrices/{date}_travel_time.csv", index = False)
