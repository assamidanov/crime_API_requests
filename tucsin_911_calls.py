import pandas as pd
import requests
import json
#from pandas.io.json import json_normalize
import numpy as np


class Incidents:
    def __init__(self, name, endpoint):
        self.df = None
        self.endpoint = endpoint
        self.name = name

    def extract(self):
        response = requests.get(url=self.endpoint)
        data = response.json()
        self.df = pd.json_normalize([i["properties"] for i in data["features"]])
        long = []
        lat = []
        for i in data["features"]:
            try:
                long.append(i["geometry"]["coordinates"][0])
                lat.append(i["geometry"]["coordinates"][1])
            except:
                long.append(np.nan)
                lat.append(np.nan)
        self.df["longitude"] = long
        self.df["latitude"] = lat


if __name__ == "__main__":
    tucson = Incidents(
        "Tucson",
        "https://opendata.arcgis.com/datasets/712c6d76150840ec85af0c52ec18f71e_47.geojson",
    )
    tucson.extract()
    print(tucson.df.head())
else:
    print("Error")

