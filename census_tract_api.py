import pandas as pd
import numpy as np

import requests
import urllib



def census_tract_request(df, start_number, end_number, lat_name, lon_name, directory, saving_rate):
    for i in range(start_number, end_number):
        try:
            params = urllib.parse.urlencode({'latitude': df.loc[i, lat_name], 'longitude':df.loc[i, lon_name], 'format':'json'})
            url = 'https://geo.fcc.gov/api/census/block/find?' + params
            response = requests.get(url)
            b = response.json()
            df.loc[i,'census_tract'] =b['Block']['FIPS']
            if (i % 100 == 0):
                print(i)
            if (i % saving_rate ==0):
                df.to_csv('%s/data.csv' % (directory))
        except:
            pass
    return df.to_csv('%s/data.csv' % (directory))

data = pd.read_csv('/Users/aassamidanov/Downloads/crime_lexisnexis_need_census_tract.csv') # enter your own directory
end_point = len(data)

census_tract_request(data, 0, end_point, 'lat', 'lon', '/Users/aassamidanov/Downloads', 10000) # enter your own directory
