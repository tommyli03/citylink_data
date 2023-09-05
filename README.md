## Requirements
Dependency can be installed using the following command:
```
poetry install
```

To activate the virtual environment, run
```
poetry shell
```

To deactivate, run
```
exit
```

## Links
- [r5py](https://r5py.readthedocs.io/en/stable/)

## Todo
### Tommy
- [ ] Configuration file with yaml [tutorial](https://betterdatascience.com/python-yaml-configuration-files/)
     - [ ] mostly folder paths
     - [ ] input to important functions
- [ ] Fix Red Line route.txt (see TODO's in the python code)
- [ ] Add GTFS for multiple transit modes
- [ ] Links:
     - [ ] Bus GTFS: (https://www.transit.land/feeds/f-dq-mtamaryland~bus/versions/8523f088e05dcd273b369dd4d65eb771c73c0a22)
     - [ ] LightRail GTFS: (https://www.transit.land/feeds/f-dq-mtamaryland~raillink/versions/c4233b29806296fc80209881fd9cec6c49fd9380)
     - [ ] CommuterBus GTFS: (https://www.transit.land/feeds/f-dq-mtamaryland~commuterbus/versions/6cc96d82827a3dfb39807521ad8a77cf8d77b368)
     - [ ] Train GTFS: (https://www.transit.land/feeds/f-dq-mtamaryland~marc/versions/32c1ab0bebce48f0f58a8110ebe245ccb5008930)
     - [ ] Subway GTFS: (https://www.transit.land/feeds/f-dq-mtamaryland~subwaylink/versions/9b0a275f899fcb67a9d2107be8b9976326507a35)

### Xinyu 
- [ ] Downstream Accessibility Calculation



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
