import pandas as pd
import numpy as np
import requests

url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"
param = {
    "f": "json",
    "singleLine": "250 N. College Park Drive, Upland, California, 91786",
    "outFields": "Match_addr,Addr_type",
}
response = requests.get(url=url, params=param)

print(response.json())