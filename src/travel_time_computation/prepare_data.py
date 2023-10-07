import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

# Works for md_rac and md_wac
def restrict_to_BaltimoreCity(df, gdf_Baltimore, geocode_col):
    df[geocode_col] = df[geocode_col].astype(str)

    df = df[(df[geocode_col].str[:5] == '24510') & (df['C000'] != 0)]

    df.loc[:, geocode_col] = df[geocode_col].astype(int)
    gdf_Baltimore.loc[:,'GEOID20'] = gdf_Baltimore['GEOID20'].astype(int)

    merged_df = gdf_Baltimore.merge(df, left_on = 'GEOID20', right_on = geocode_col)
    merged_df['id'] = merged_df[geocode_col]

    return merged_df[['geometry', 'C000', 'id']]


def set_geometry(gdf):
    # Convert latitude and longitude columns to float data types
    gdf.loc[:,'INTPTLAT20'] = gdf['INTPTLAT20'].astype(float)
    gdf.loc[:,'INTPTLON20'] = gdf['INTPTLON20'].astype(float)
    gdf['geometry'] = gdf.apply(lambda row: Point(row['INTPTLON20'], row['INTPTLAT20']), axis=1)
    return gdf


def prepare_data_Baltimore(shapefile_path, md_rac_path, md_wac_path):
    # Read in shapefile for block groups in Maryland
    block_gdf = gpd.read_file(shapefile_path)
    block_gdf = set_geometry(block_gdf)

    #Restrict to Baltimore City
    gdf_Baltimore = block_gdf[block_gdf['COUNTYFP20'] == '510']

    gdf_Baltimore.loc[:,'GEOID20'] = gdf_Baltimore['GEOID20'].astype(int)

    md_rac_df = restrict_to_BaltimoreCity(pd.read_csv(md_rac_path), gdf_Baltimore, 'h_geocode')
    md_wac_df = restrict_to_BaltimoreCity(pd.read_csv(md_wac_path), gdf_Baltimore, 'w_geocode')

    return md_rac_df, md_wac_df
