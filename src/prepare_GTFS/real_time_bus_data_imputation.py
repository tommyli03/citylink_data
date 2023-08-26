import pandas as pd
import os
from tqdm import tqdm
import shutil
from src.prepare_GTFS.util import *

# TODO: correct all the paths
# TODO: add bus_data_csv_path and gtfs_stop_times_path to the function into the config file
bus_data_csv_path = 'processed_data/bus_accurate_data.csv'
gtfs_stop_times_path = 'transitland/stop_times.txt'

gtfs_stop_times = pd.read_csv(gtfs_stop_times_path)

observed_times = pd.read_csv(bus_data_csv_path)
unique_dates = observed_times['date'].unique()
observed_times_by_date = {}
for date in unique_dates:
    observed_times_by_date[date] = observed_times[observed_times['date'] == date]

print("Imputing partially missing times:")
os.makedirs('stop_times_temp', exist_ok=True)  
file_paths = []
for date, stop_times_df in tqdm(observed_times_by_date.items()):
    stop_times_df = gtfs_stop_times.merge(stop_times_df, on=['trip_id', 'stop_id'], how="left")
    stop_times_df = stop_times_df[stop_times_df['scheduled_visit_time'].notna()]
    stop_times_df['arrival_time'] = stop_times_df['observed_visit_time']

    stop_times_df = stop_times_df.groupby("trip_id").apply(impute_partial_times)
    stop_times_df['departure_time'] = stop_times_df['arrival_time']

    stop_times_df.drop(columns=['date', 'scheduled_visit_time', 'observed_visit_time', 'trip_distance_traveled'], inplace=True)

    stop_times_df.to_csv(f'stop_times_temp/{date}.txt', index=False)
    
    file_paths.append(f'{date}.txt')


print("Imputing fully missing times:")
updated_stop_times_folder = "stop_times_updated"
os.makedirs(updated_stop_times_folder, exist_ok=True)  

for file in tqdm(file_paths):
    df = pd.read_csv(f'stop_times_temp/{file}')
    trip_ids_to_replace = df.loc[df.arrival_time.isna()].trip_id.unique()
    for trip_id in trip_ids_to_replace:
        new_data = impute_full_times(trip_id, file_paths)
        df = df.loc[df.trip_id != trip_id]
        df = df.append(new_data)
    df.to_csv(f'{updated_stop_times_folder}/{file}', index=False)

shutil.rmtree('stop_times_temp/')

transitland_folder = 'transitland'
copy_folder = 'transitland_copy/'
zipfiles_folder = 'updated_gtfs'
os.makedirs(zipfiles_folder, exist_ok=True)  

print("Creating GTFS zip files:")

for filename in tqdm(os.listdir(updated_stop_times_folder)):
    shutil.copytree(transitland_folder, copy_folder)
    times = pd.read_csv(f"{updated_stop_times_folder}/{filename}")
    trips = pd.read_csv(f'{copy_folder}trips.txt')

    unique_trip_ids = times['trip_id'].unique()
    trips = trips[trips['trip_id'].isin(unique_trip_ids)]
    routes = pd.read_csv(f"{copy_folder}routes.txt")
    unique_route_ids = trips['route_id'].unique()
    routes = routes[routes['route_id'].isin(unique_route_ids)]
    directions = pd.read_csv(f"{copy_folder}directions.txt")
    directions = directions[directions['route_id'].isin(unique_route_ids)]


    trips.to_csv(f'{copy_folder}trips.txt', index=False)
    times.to_csv(f'{copy_folder}stop_times.txt', index=False)
    routes.to_csv(f"{copy_folder}routes.txt", index=False)
    directions.to_csv(f"{copy_folder}directions.txt", index=False)

    zip_filename = f'{os.path.splitext(filename)[0]}'
    zip_path = os.path.join(zipfiles_folder, zip_filename)
    shutil.make_archive(zip_path, 'zip', copy_folder)
    shutil.rmtree(copy_folder)

shutil.rmtree(updated_stop_times_folder)