## Requirements
Dependency can be installed using the following command:
```
pip install -r requirements.txt
```

## Directory Tree
```md
.
├── README.md
├── output.zip
├── processed_data
│   ├── bus_accurate_data.csv
│   ├── redline.zip
│   └── updated_gtfs
│       ├── 2023-02-08.zip
│       ├── 2023-02-09.zip
│       ├── 2023-02-14.zip
│       ├── 2023-02-15.zip
│       ├── 2023-02-28.zip
│       ├── 2023-03-06.zip
│       ├── 2023-03-17.zip
│       ├── 2023-03-28.zip
│       ├── 2023-04-07.zip
│       └── 2023-04-20.zip
├── raw_data
│   ├── Baltimore Red Line- Alignment.csv
│   ├── Baltimore Red Line- Stations.csv
│   ├── block_group
│   │   ├── tl_2020_24_tabblock20.cpg
│   │   ├── tl_2020_24_tabblock20.dbf
│   │   ├── tl_2020_24_tabblock20.prj
│   │   ├── tl_2020_24_tabblock20.shp
│   │   ├── tl_2020_24_tabblock20.shp.ea.iso.xml
│   │   ├── tl_2020_24_tabblock20.shp.iso.xml
│   │   ├── tl_2020_24_tabblock20.shx
│   │   └── tl_2020_24_tabblock20.zip
│   ├── bus_accurate_data.csv
│   ├── maryland-latest.osm.pbf
│   ├── md_rac_S000_JT00_2020.csv.gz
│   ├── md_wac_S000_JT00_2020.csv.gz
│   └── transitland
│       ├── agency.txt
│       ├── calendar.txt
│       ├── calendar_attributes.txt
│       ├── calendar_dates.txt
│       ├── directions.txt
│       ├── feed_info.txt
│       ├── routes.txt
│       ├── shapes.txt
│       ├── stop_times.txt
│       ├── stops.txt
│       └── trips.txt
├── redline
│   ├── agency.txt
│   ├── calendar.txt
│   ├── calendar_attributes.txt
│   ├── calendar_dates.txt
│   ├── directions.txt
│   ├── feed_info.txt
│   ├── routes.txt
│   ├── shapes.txt
│   ├── stop_times.txt
│   ├── stops.txt
│   └── trips.txt
├── requirements.txt
├── src
│   ├── prepare_GTFS
│   │   ├── add_red_line.py
│   │   ├── configs
│   │   │   └── config.yaml
│   │   └── real_time_bus_data_imputation.py
│   ├── proprocessing
│   │   └── preprocessing.py
│   └── travel_time_computation
│       ├── prepare_data.py
│       ├── travel_time_Baltimore.py
│       └── travel_time_computation.py
├── transit.ipynb
└── util.py

12 directories, 60 files
(aaforecast) yangxinyuxie@Yangxinyus-MacBook-Pro citylink_data % tree .
.
├── README.md
├── output.zip
├── processed_data
│   ├── bus_accurate_data.csv
│   ├── redline.zip
│   └── updated_gtfs
│       ├── 2023-02-08.zip
│       ├── 2023-02-09.zip
│       ├── 2023-02-14.zip
│       ├── 2023-02-15.zip
│       ├── 2023-02-28.zip
│       ├── 2023-03-06.zip
│       ├── 2023-03-17.zip
│       ├── 2023-03-28.zip
│       ├── 2023-04-07.zip
│       └── 2023-04-20.zip
├── raw_data
│   ├── Baltimore Red Line- Alignment.csv
│   ├── Baltimore Red Line- Stations.csv
│   ├── block_group
│   │   ├── tl_2020_24_tabblock20.cpg
│   │   ├── tl_2020_24_tabblock20.dbf
│   │   ├── tl_2020_24_tabblock20.prj
│   │   ├── tl_2020_24_tabblock20.shp
│   │   ├── tl_2020_24_tabblock20.shp.ea.iso.xml
│   │   ├── tl_2020_24_tabblock20.shp.iso.xml
│   │   ├── tl_2020_24_tabblock20.shx
│   │   └── tl_2020_24_tabblock20.zip
│   ├── bus_accurate_data.csv
│   ├── maryland-latest.osm.pbf
│   ├── md_rac_S000_JT00_2020.csv.gz
│   ├── md_wac_S000_JT00_2020.csv.gz
│   └── transitland
│       ├── agency.txt
│       ├── calendar.txt
│       ├── calendar_attributes.txt
│       ├── calendar_dates.txt
│       ├── directions.txt
│       ├── feed_info.txt
│       ├── routes.txt
│       ├── shapes.txt
│       ├── stop_times.txt
│       ├── stops.txt
│       └── trips.txt
├── redline
│   ├── agency.txt
│   ├── calendar.txt
│   ├── calendar_attributes.txt
│   ├── calendar_dates.txt
│   ├── directions.txt
│   ├── feed_info.txt
│   ├── routes.txt
│   ├── shapes.txt
│   ├── stop_times.txt
│   ├── stops.txt
│   └── trips.txt
├── requirements.txt
├── src
│   ├── prepare_GTFS
│   │   ├── add_red_line.py
│   │   ├── configs
│   │   │   └── config.yaml
│   │   ├── real_time_bus_data_imputation.py
│   │   └── util.py
│   ├── proprocessing
│   │   └── preprocessing.py
│   └── travel_time_computation
│       ├── prepare_data.py
│       ├── travel_time_Baltimore.py
│       └── travel_time_computation.py
└── transit.ipynb
```