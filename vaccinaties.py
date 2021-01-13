import streamlit as st
import pandas as pd
import numpy as np
import datetime

current_date = datetime.datetime.now()
week_number = current_date.strftime("%V").lstrip("0")
number_of_day = current_date.weekday()
start_of_week = current_date - datetime.timedelta(days=number_of_day)
end_of_week = current_date + datetime.timedelta(days=(7 - number_of_day - 1))


welcome_text = """
# Vaccinaties in Vlaanderen

Onderstaande kaart toont de locatie van de WZC's in Vlaanderen die in week """ + week_number + """ (""" + start_of_week.strftime("%d/%m/%Y") + """ - """ + end_of_week.strftime("%d/%m/%Y") + """) het vaccin zullen krijgen. 
"""

welcome_text

df = pd.read_excel(
    "https://github.com/MiDeCo86/Vaccinaties-overzicht/blob/main/Vaccinaties.xlsx?raw=true",
    sheet_name="data"
)

df2 = df.copy()
values_to_drop = ["NaN"]
valid_longititudes = df2["lon"].notna()
valid_latitudes = df2["lat"].notna()
df2 = df[valid_longititudes & valid_latitudes]
df3 = df2.copy()
show_raw_data = False

min_date = df["Datum"].min().date()
max_date = df["Datum"].max().date()

st.sidebar.subheader("Criteria:")

datum = st.sidebar.date_input("Selecteer je gewenste datum: ", current_date.date(), min_date, max_date)

option = st.sidebar.selectbox("Selecteer je gemeente: ", df["Gemeente"].unique())

if option != "Alle":
    df3 = df2[df2["Gemeente"] == option]

if datum:
    df3 = df3[df3["Datum"].dt.date == datum]

st.sidebar.subheader("Pure data:")
if st.sidebar.checkbox("Toon pure data"):   
    show_raw_data = not show_raw_data

st.sidebar.subheader("Extra:")
if st.sidebar.button("Toon alle geplande vaccinaties"):
    df3 = df2.copy()

coordinates = {
    "lat": df3["lat"],
    "lon": df3["lon"]
}

map_data = pd.DataFrame(coordinates, columns=["lat", "lon"])

st.markdown("### Kaartgegevens:")
st.map(map_data)

missing_values = len(df) - len(df2)

st.markdown("_" + str(missing_values) + " plaatsen kunnen niet getoond worden op de kaart wegens ontbrekende coördinaten._" )

if show_raw_data:
    st.markdown("### Datagegevens:")
    df3