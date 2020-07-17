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

response_json = response.json()
response_json['candidates'][0]['location']['x']
response_json['candidates'][0]['location']['y']
response_json['candidates'][0]['score']