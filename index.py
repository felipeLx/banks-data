import streamlit as st
import json
import pandas as pd

st.title('Latam Banks Details')

st.sidebar.title("Filter the Country and Bank to show details")

tab1, tab2 = st.tabs(["Limits", "Better Option"])
tab1.write("Limits and How to handle")
tab2.write("Better option for payment")

country_selectbox = st.sidebar.selectbox(
    "Select the Country",
    ("Mexico", "Peru", "Colombia")
)

bank_selectbox = st.sidebar.selectbox(
    "Select the Bank",
    ("BBVA", "Banregio", "Volaris Invex", "HSBC", "Santander", "Bancoppel")
)

with open('banks.json', 'r') as jf:
    json_file = json.load(jf)
    for row in json_file["Countries"]:
        for detail in row['Banks']:
            if row['Country'] == country_selectbox and detail['Bank'] == bank_selectbox:    
                for options in detail['Limits']:
                    tab1.write(row['Country'])
                    tab1.write(detail['Bank'])
                    tab1.write(options['Text'])
                    tab1.write('Currency: ' + options['Currency'])
                    tab1.write('Per day: ' +  options['Per day'])
                    tab1.write('Per month: ' +  options['Monthly'])
                    for i in options['handling']:
                        tab1.image(i)
                
                    tab2.write(row['Country'])
                    tab2.write(detail['Bank'])
                    for i in options['Digital card']:
                        tab2.write(i)
    

