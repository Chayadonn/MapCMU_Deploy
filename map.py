import streamlit as st

import plotly.express as px
import pandas as pd

def plot_map(dff):
    # Month out
    fig = px.scatter_mapbox(dff, lat="lat", lon="long", color="gate_out", size="gate_out", text="gate name", title='จำนวนรถออกแต่ละประตู',
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=20, zoom=13,
                            mapbox_style="carto-positron")
    # Month in
    fig2 = px.scatter_mapbox(dff, lat="lat", lon="long", color="gate_in", size="gate_in", text="gate name", title='จำนวนรถเข้าแต่ละประตู',
                            color_continuous_scale=px.colors.cyclical.Edge, size_max=20, zoom=13,
                            mapbox_style="carto-positron")
    # num of car
    fig3 = px.scatter_mapbox(dff, lat="lat", lon="long", color="num_car", size="num_car", text="gate name", title='จำนวนรถยนต์เข้า-ออกแต่ละประตู',
                            color_continuous_scale=px.colors.cyclical.Phase, size_max=20, zoom=13,
                            mapbox_style="carto-positron")
    # num of moto
    fig4 = px.scatter_mapbox(dff, lat="lat", lon="long", color="num_moto", size="num_moto", text="gate name", title='จำนวนรถจักรยานยนต์เข้า-ออกแต่ละประตู',
                            color_continuous_scale=px.colors.cyclical.HSV, size_max=20, zoom=13,
                            mapbox_style="carto-positron")
    tab1, tab2, tab3, tab4 = st.tabs(["จำนวนรถที่ออกแต่ละประตู", "จำนวนรถที่เข้าแต่ละประตู", "จำนวนรถยนต์เข้า-ออกแต่ละประตู", "จำนวนรถจักรยานยนต์เข้า-ออกแต่ละประตู"])
    # Plot each tab
    with tab1:
        st.plotly_chart(fig, use_container_width=False, theme='streamlit', width=15000, height=600)
    with tab2:
        st.plotly_chart(fig2, use_container_width=False, theme='streamlit', width=15000, height=600)
    with tab3:
        st.plotly_chart(fig3, use_container_width=False, theme='streamlit', width=15000, height=600)
    with tab4:
        st.plotly_chart(fig4, use_container_width=False, theme='streamlit', width=15000, height=600)
    
    on = st.toggle('Show summary table')
    if on:
        st.table(dff)

if __name__ == "__main__":
    st.title(':violet[CMU] MAP 2023:sunglasses:')
    dff = pd.read_csv('car (1).csv')

    option = st.selectbox(
        "What month would you like to select?",
        ("January", "February", "March", "April", "May", "June"),
        index=None,
        placeholder="Select month...",
    )
    st.write('You selected:', option)
    
    if option == "January":
        
        lat = list(dff['lat'])
        long = list(dff['long'])
        gate_out_nameMonth = list(dff['o-M_1'])
        gate_in_Month = list(dff['i-M_1'])
        num_of_car = list(dff['car-M_1'])
        num_of_moto = list(dff['motorcycle-M_1'])
        gate_name = list(dff['gate_name'])
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)

    elif option == 'February':
        lat = list(dff['lat'])
        long = list(dff['long'])
        gate_out_nameMonth = list(dff['o-M_2'])
        gate_in_Month = list(dff['i-M_2'])
        num_of_car = list(dff['car-M_2'])
        num_of_moto = list(dff['motorcycle-M_2'])
        gate_name = list(dff['gate_name'])
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)

    elif option == 'March':
        lat = list(dff['lat'])
        long = list(dff['long'])
        gate_out_nameMonth = list(dff['o-M_3'])
        gate_in_Month = list(dff['i-M_3'])
        num_of_car = list(dff['car-M_3'])
        num_of_moto = list(dff['motorcycle-M_3'])
        gate_name = list(dff['gate_name'])
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)

    elif option == 'April':
        lat = list(dff['lat'])
        long = list(dff['long'])
        gate_out_nameMonth = list(dff['o-M_4'])
        gate_in_Month = list(dff['i-M_4'])
        num_of_car = list(dff['car-M_4'])
        num_of_moto = list(dff['motorcycle-M_4'])
        gate_name = list(dff['gate_name'])
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)
    
    elif option == 'May':
        lat = list(dff['lat'])
        long = list(dff['long'])
        gate_out_nameMonth = list(dff['o-M_5'])
        gate_in_Month = list(dff['i-M_5'])
        num_of_car = list(dff['car-M_5'])
        num_of_moto = list(dff['motorcycle-M_5'])
        gate_name = list(dff['gate_name'])
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)
     
    elif option == 'June':
        lat = list(dff['lat'])
        long = list(dff['long'])
        gate_out_nameMonth = list(dff['o-M_6'])
        gate_in_Month = list(dff['i-M_6'])
        num_of_car = list(dff['car-M_6'])
        num_of_moto = list(dff['motorcycle-M_6'])
        gate_name = list(dff['gate_name'])
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)

    

