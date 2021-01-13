# %%
import pandas as pd
import numpy as np
import urllib
import json

"""
input: original excel with data from laat je vaccineren. If there is only a pdf available use a pdf to excel converter to retrieve the excel
ouput: excel with two extra columns. This can be used as input for the main program
This program will add coordinates to the existing data so it can be used to visualize the data on the streamlit map
Two extra columns will be created lon (longitude) and lat (latitude)
"""

df = pd.read_excel(
    "<path to excel here>", sheet_name="data"
)


# %%

base_url = "https://nominatim.openstreetmap.org/search.php?q="
url_format = "&format=jsonv2"
lon = []
lat = []

for index, row in df.iterrows():
    address = str(row["Nummer"]) + " " + str(row["Straat"]) + "," + str(row["Gemeente"]) + "," + "Belgium"
    url = base_url + urllib.parse.quote_plus(address) + url_format

    result = json.load(urllib.request.urlopen(url))
    try:
        lon.append(result[0]["lon"])
    except IndexError:
        lon.append("NaN")

    try:
        lat.append(result[0]["lat"])
    except IndexError:
        lat.append("NaN")


df["lon"] = lon
df["lat"] = lat

df.to_excel("Vaccinaties.xlsx", sheet_name="data")

# https://nominatim.openstreetmap.org/search.php?q=87%20schauwegemstraat%2Cmelle%2Cbelgium&polygon_geojson=1&format=jsonv2

# %%

# %%
