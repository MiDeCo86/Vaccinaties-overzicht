# %%
import pandas as pd
import numpy as np
import urllib
import json

df = pd.read_excel(
    "<path to input excel>", sheet_name="Table 4", engine="openpyxl"
)

df.dtypes
# %%

def convert_na_to_empty(column_from_row):
    if pd.isna(column_from_row):
        return ""
    else:
        return str(column_from_row)

streets = []
house_numbers = []
townships = []
for index, row in df.iterrows():

    streets.append(convert_na_to_empty(row["Kolom1"]) + convert_na_to_empty(row["Kolom2"]) + convert_na_to_empty(row["Straat"]))
    house_numbers.append(convert_na_to_empty(row["kolom3"]) + convert_na_to_empty(row["Kolom4"]) + convert_na_to_empty(row["Nummer"]))
    townships.append(convert_na_to_empty(row["Kolom5"]) + convert_na_to_empty(row["Gemeente"]))


# little check before proceeding to save the new dataframe
length_of_dataframe = df.shape[0]

assert len(streets) == length_of_dataframe
assert len(house_numbers) == length_of_dataframe
assert len(townships) == length_of_dataframe

# %%
columns = ["Datum", "WZC", "Straat", "Nummer", "Plaats", "Gemeente", "Totaal1", "Totaal2", "Totaal2"]

df2 = df[["Datum", "WZC", "Plaats", "totaal1", "totaal2", "totaal3"]].copy()

df2["Straat"] = streets
df2["Nummer"] = house_numbers
df2["Gemeente"] = townships

df2.to_excel("<name output excel>", sheet_name="data")

# %%
import pandas as pd
import numpy as np
import urllib
import json

df = pd.read_excel(
    "<path to input excel>", sheet_name="Table 4", engine="openpyxl"
)

df.dtypes
# %%

streets = []
house_numbers = []
townships = []
for index, row in df.iterrows():

    streets.append(convert_na_to_empty(row["Kolom1"]) + convert_na_to_empty(row["Kolom2"]) + convert_na_to_empty(row["Kolom3"]) + convert_na_to_empty(row["Kolom4"]) + convert_na_to_empty(row["Straat"]))
    house_numbers.append(convert_na_to_empty(row["Kolom5"]) + convert_na_to_empty(row["Kolom6"]) + convert_na_to_empty(row["Kolom7"]) + convert_na_to_empty(row["Nummer"]))
    townships.append(convert_na_to_empty(row["Kolom9"]) + convert_na_to_empty(row["Kolom10"]) + convert_na_to_empty(row["Gemeente"]))

length_of_dataframe = df.shape[0]

assert len(streets) == length_of_dataframe
assert len(house_numbers) == length_of_dataframe
assert len(townships) == length_of_dataframe

df3 = df[["Datum", "WZC", "Plaats", "Totaal1", "Totaal2", "Totaal3"]].copy()

df3["Straat"] = streets
df3["Nummer"] = house_numbers
df3["Gemeente"] = townships

df3.to_excel("<name output excel>", sheet_name="data")

# %%
