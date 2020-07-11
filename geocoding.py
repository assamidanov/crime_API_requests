import pandas as pd
import numpy as np



from arcgis.gis import GIS
from arcgis.geocoding import geocode, reverse_geocode
from arcgis.geometry import Point

gis = GIS()


def geocoding(df, start_number, end_number, address_var, directory, saving_rate):
# 	for i in range(start_number, end_number):
# 		if (i % 100 == 0):
# 			print(i)
# 		if (i % saving_rate ==0):
# 			df.to_csv('%s/data.csv' % (directory))
# 		try:
# 			geo = {
# 			'Address': df.loc[i,address_var]
# 			}
# 			result = geocode(geo)
# 			df.loc[i,'lat'] = result[0]['location']['y']
# 			df.loc[i,'lon'] = result[0]['location']['x']
# 			df.loc[i,'zipcode'] = result[0]['attributes']['Postal']
# 		except:
# 			pass
# 	return df.to_csv('%s/data.csv' % (directory))


# data = pd.read_csv('/Users/aassamidanov/Downloads/crime_lexisnexis_need_census_tract.csv') # enter your own directory
# end_point = len(data)ƒ

# geocoding(data, 0, end_point , 'address', '/Users/aassamidanov/Downloads', 10000) # enter your own directory

# you can firstly check with 100 rows, to select whole data put len(data)
