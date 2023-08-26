import geopandas as gpd
import pandas as pd

# Works for md_rac and md_wac
def restrict_to_BaltimoreCity(df, gdf_Baltimore, geocode_col):
    df[geocode_col] = df[geocode_col].astype(str)

    df = df[(df[geocode_col].str[:5] == '24510') & (df['C000'] != 0)]

    df[geocode_col] = df[geocode_col].astype(int)

    merged_df = gdf_Baltimore.merge(df, left_on = 'GEOID20', right_on = geocode_col)
    merged_df['id'] = merged_df[geocode_col]

    return merged_df


def prepare_data_Baltimore(shapefile_path, md_rac_path, md_wac_path):
    block_gdf = gpd.read_file(shapefile_path)
    block_gdf.geometry = block_gdf.geometry.centroid

    #Restrict to Baltimore City
    gdf_Baltimore = block_gdf[block_gdf['COUNTYFP20'] == '510']

    gdf_Baltimore['GEOID20'] = gdf_Baltimore['GEOID20'].astype(int)

    md_rac_df = restrict_to_BaltimoreCity(pd.read_csv(md_rac_path), 'h_geocode')
    md_wac_df = restrict_to_BaltimoreCity(pd.read_csv(md_wac_path), 'w_geocode')

    return md_rac_df, md_wac_df
