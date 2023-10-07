import pandas as pd
import os
from datetime import timedelta
from src.util import get_config

config = get_config()
processed_path = 'processed_data/'

if __name__ == "__main__":
    
    begin_date = config['begin_date']
    end_date = config['end_date']

    # Define the step (in this case, one day)
    step = timedelta(days=1)

    # Iterate through dates from begin_date to end_date
    current_date = begin_date

    file_paths = []
    while current_date <= end_date:
        date = current_date.strftime('%Y-%m-%d')
        current_date += step

        dir_path = processed_path + f"job_accessibility/S000/{0}/red_line/{date}/45.csv"

        if os.path.exists(dir_path):
            file_paths.append(dir_path)

    all_data = pd.concat([pd.read_csv(file) for file in file_paths], ignore_index=True)

    # Compute the median job accessibility for each h_geocode
    median_accessibility = all_data.groupby('h_geocode')['gravity'].median().reset_index()
    median_accessibility.to_csv('median_accessibility_after.csv', index=False)
