import streamlit as st

import plotly.express as px
import pandas as pd


if __name__ == "__main__":
       info = [{'centroid_lat': 18.8071978, 'centroid_lon':98.9626453, 'car_hours':100 , 'peak_hour':2.8}, 
              {'centroid_lat': 18.8071978, 'centroid_lon':98.9626453, 'car_hours':1200 , 'peak_hour':2},
              {'centroid_lat': 18.796642425064054, 'centroid_lon':98.95349937696828, 'car_hours':1700 , 'peak_hour':2.4}]
       df = pd.DataFrame(info)
       fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                     color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                     mapbox_style="carto-positron")

