import pandas as pd
import geopandas as gpd


shapefile_path = 'raw_data/tl_2020_24_tabblock20.shp'
md_rac_path = 'raw_data/md_rac_S000_JT00_2020.csv.gz'
md_wac_path = 'raw_data/md_wac_S000_JT00_2020.csv.gz'


from prepare_data import prepare_data_Baltimore

md_rac_df, md_wac_df = prepare_data_Baltimore(shapefile_path, md_rac_path, md_wac_path)

