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
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=20, zoom=13,
                            mapbox_style="carto-positron")
    # num of moto
    fig4 = px.scatter_mapbox(dff, lat="lat", lon="long", color="num_moto", size="num_moto", text="gate name", title='จำนวนรถจักรยานยนต์เข้า-ออกแต่ละประตู',
                            color_continuous_scale=px.colors.cyclical.Edge, size_max=20, zoom=13,
                            mapbox_style="carto-positron")
    tab1, tab2, tab3, tab4 = st.tabs(["จำนวนรถออกแต่ละประตู", "จำนวนรถเข้าแต่ละประตู", "จำนวนรถยนต์เข้า-ออกแต่ละประตู", "จำนวนรถจักรยานยนต์เข้า-ออกแต่ละประตู"])
    with tab1:
        st.plotly_chart(fig, use_container_width=False, theme='streamlit', width=1500, height=600)
    with tab2:
        st.plotly_chart(fig2, use_container_width=False, theme='streamlit', width=1500, height=600)
    with tab3:
        st.plotly_chart(fig3, use_container_width=False, theme='streamlit', width=1500, height=600)
    with tab4:
        st.plotly_chart(fig4, use_container_width=False, theme='streamlit', width=1500, height=600)

if __name__ == "__main__":
    st.title(':violet[CMU] MAP :sunglasses:')
    dff = pd.read_csv('car.csv')

    gate = {'วิศวกรรมศาสตร์': 4174653,
            'แยก อมช': 2898242,
            'แยกบริหาร': 2264162,
            'เกษตรศาสตร์': 1396926,
            'วงเวียนหอนาฬิกา': 5167441,
            'หน้ามหาวิทยาลัย': 3107747,
            'วงเวียนสนามเทนนิส': 1497873,
            'วงเวียนมนุษย์': 1115321,
            'แยกโรงอาหารใหม่': 911818,
            'สวนดอกพาร์ค': 450524,
            'วงเวียน SCB': 2362633,
            'วงเวียนอ่างตาดชมพู': 1089555,
            'วิศวกรรมศาสตร์ใหม่': 263159,
            'คันคลองชลประทาน': 3194781,
            'แยกอ่างแก้ว': 862643,
            'แยกประตูไผ่ล้อม': 975056,
            'ไผ่ล้อม': 244993,
            'ลานจอดรถ อมช': 92024,
            'ลานจอดรถฝายหิน': 567744,
            'POC-ENG-in': 19577,
            'แยกตึกอธิการบดี': 531776,
            'ศึกษาศาสตร์': 72586,
            'ลานจอดรถ  S1': 53026,
            'ปตท.ใหม่': 548877,
            'ลานจอดรถไร่ฟอร์ด': 50374,
            'ลานจอดรถหอ 40 ปี': 31219,
            'ลานจอดรถหน้ามอ': 110571,
            'จอดรถโรงอาหารกลาง': 75654,
            'อาคารสำนักงาน 3': 22147,
            'ข่วงพยอม': 1159}
    
    option = st.selectbox(
        "What month would you like to select?",
        ("January", "February", "March", "April", "May", "June"),
        index=None,
        placeholder="Select month...",
    )
    st.write('You selected:', option)

    coor = [(18.793383392039146, 98.95333379108743), (18.799566391546588, 98.9533094270958), (18.795957161465292, 98.95724241090699), (18.79171479533299, 98.95879560971413), (18.796576057863906, 98.9532826556333), (18.808277546950226, 98.95463338683885), (18.799530189229277, 98.95545297967308), (18.80267229218127, 98.95153342416431), (18.799442513831558, 98.95190873634111), (18.78999549520462, 98.97096228612112), (18.803899913625923, 98.95388106655491), (18.803916297724793, 98.94904676538084), (18.794274483304857, 98.95035038949155), (18.795345102354286, 98.96170678168215), (18.805032997209665, 98.9504519097645),
            (18.801370518953103, 98.95665780068265), (18.801101919428785, 98.95739818263235), (18.800383655508554, 98.95368047163448), (18.7997525526264, 98.94884952861116), (18.795583346617565, 98.95860079330882), (18.805539021855953, 98.95548922372875), (18.79304544951939, 98.95451932140443), (18.79238184497654, 98.95748162239498), (18.796731194349526, 98.96133103728313), (18.793876495552567, 98.9633310637738), (18.79857168849546, 98.95879773748997), (18.807695484637776, 98.9552865829107), (18.799111250877964, 98.95217939144588), (18.803733192640728, 98.95564660146975), (18.791212918521417, 98.96400071057825)]
    
    if option == "January":
        lat = [coor[x][0] for x in range(len(coor))]
        long = [coor[x][1] for x in range(len(coor))]
        gate_out_nameMonth = list(dff['o-M_1'])
        gate_in_Month = list(dff['i-M_1'])
        num_of_car = list(dff['car-M_1'])
        num_of_moto = list(dff['motorcycle-M_1'])
        gate_name = list(gate.keys())
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)

    elif option == 'February':
        lat = [coor[x][0] for x in range(len(coor))]
        long = [coor[x][1] for x in range(len(coor))]
        gate_out_nameMonth = list(dff['o-M_2'])
        gate_in_Month = list(dff['i-M_2'])
        num_of_car = list(dff['car-M_2'])
        num_of_moto = list(dff['motorcycle-M_2'])
        gate_name = list(gate.keys())
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)

    elif option == 'March':
        lat = [coor[x][0] for x in range(len(coor))]
        long = [coor[x][1] for x in range(len(coor))]
        gate_out_nameMonth = list(dff['o-M_3'])
        gate_in_Month = list(dff['i-M_3'])
        num_of_car = list(dff['car-M_3'])
        num_of_moto = list(dff['motorcycle-M_3'])
        gate_name = list(gate.keys())
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)

    elif option == 'April':
        lat = [coor[x][0] for x in range(len(coor))]
        long = [coor[x][1] for x in range(len(coor))]
        gate_out_nameMonth = list(dff['o-M_4'])
        gate_in_Month = list(dff['i-M_4'])
        num_of_car = list(dff['car-M_4'])
        num_of_moto = list(dff['motorcycle-M_4'])
        gate_name = list(gate.keys())
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)
    
    elif option == 'May':
        lat = [coor[x][0] for x in range(len(coor))]
        long = [coor[x][1] for x in range(len(coor))]
        gate_out_nameMonth = list(dff['o-M_5'])
        gate_in_Month = list(dff['i-M_5'])
        num_of_car = list(dff['car-M_5'])
        num_of_moto = list(dff['motorcycle-M_5'])
        gate_name = list(gate.keys())
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)
     
    elif option == 'June':
        lat = [coor[x][0] for x in range(len(coor))]
        long = [coor[x][1] for x in range(len(coor))]
        gate_out_nameMonth = list(dff['o-M_6'])
        gate_in_Month = list(dff['i-M_6'])
        num_of_car = list(dff['car-M_6'])
        num_of_moto = list(dff['motorcycle-M_6'])
        gate_name = list(gate.keys())
        dff = pd.DataFrame({'gate name': gate_name, 'lat': lat,
                        'long': long, 'gate_out': gate_out_nameMonth, 'gate_in':gate_in_Month, 'num_car':num_of_car, 'num_moto':num_of_moto})
        plot_map(dff)
    

    

