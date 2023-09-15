import pandas as pd
import os

processed_path = 'processed_data/'

def impedance(time, thresh):
    return max((thresh * 2) / (thresh + time) - 1, 0)

modes = ['transit_current', 'red_line']
time_col = {'transit_current': 'travel_time_before', 'red_line': 'travel_time_after'}

def compute_job_accessibility(travel_time, job_totals, seg, assumed_train_speed, min_thresh, max_thresh, thresh_step, date):

    df = job_totals.merge(travel_time, left_on="w_geocode", right_on="to_id")

    df.drop("w_geocode", axis=1, inplace=True)
    df.rename(columns={"from_id": "h_geocode",}, inplace=True)

    for mode in modes:
        for thresh in range(min_thresh, max_thresh + thresh_step, thresh_step):
            below_df = df[df[time_col[mode]] <= thresh].copy()
            below_df["gravity"] = below_df[time_col[mode]].apply(lambda t: impedance(t, thresh))
            below_df["gravity"] = below_df["gravity"] * below_df["job_totals"]

            final_df = below_df[['h_geocode', 'job_totals', 'gravity']].groupby('h_geocode').sum()

            dir_path = processed_path + f"job_accessibility/{seg}/{int(assumed_train_speed)}/{mode}/{date}"

            os.makedirs(dir_path, exist_ok=True)

            final_df.to_csv(f"{dir_path}/{int(thresh)}.csv")


date = '2023-05-31'
transit_time = pd.read_csv(f'processed_data/travel_time_matrices/{date}_travel_time.csv')
transit_time = transit_time.fillna(9999)

job_totals = pd.read_csv('processed_data/job_totals_tract_S000.csv')
seg = 'S000'
speed = 0
min_thresh = 30
max_thresh = 60
thresh_step = 15


compute_job_accessibility(transit_time, job_totals, seg, speed,
                          min_thresh, max_thresh,
                          thresh_step, date)