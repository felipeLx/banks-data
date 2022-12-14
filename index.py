from queue import Empty
import streamlit as st
import json
import pandas as pd
from streamlit.components.v1 import components, html

st.title('Latam Banks Details')

st.sidebar.title("Filter the Country and Bank to show details")

tab0, tab1, tab2, tab3, tab4 = st.tabs(["PSP Dashboard", "Limits", "Better Option", "Manual Limits", "Payretailers"])
tab0.write("Rafinita Dashboard")
tab1.write("Limits and How to handle")
tab2.write("Better option for payment")
tab3.write("Manual Payment Limits: Transaction and Daily / Monthly")
tab4.write("Payretailers - Handle Manual Payments")

country_selectbox = st.sidebar.selectbox(
    "Select the Country",
    ("Mexico", "Peru", "Colombia")
)

if country_selectbox == 'Mexico':
    bank_selectbox = st.sidebar.selectbox(
        "Select the Bank",
        ("BBVA", "Banregio", "Volaris Invex", "HSBC", "Santander", "Bancoppel", "Citibanamex", "Afirme", "Inbursa", "Scotiabank", "Banorte")
    )

if country_selectbox == 'Peru':
    bank_selectbox = st.sidebar.selectbox(
        "Select the Bank",
        ("BBVA", "BCP", "Scotiabank", "Interbank", "Banco Pichincha", "MiBanco", "Banco Falabella", "Banco de Comercio", "Banco GNB", "Banco Ripley")
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
                        if i:
                            tab1.image(i)
                
                    tab2.write(row['Country'])
                    tab2.write(detail['Bank'])
                    for i in options['Digital card']:
                        if i:
                            tab2.write(i)
                    for i in options['Pics']:
                        if i:
                            tab2.image(i)
                    
                    tab3.write(row['Country'])
                    tab3.image(row['Payretailers'])
                    tab3.image('./images/a-manual.PNG')

                    for types in row["Manual"]:
                        tab4.write(types['Cash Pmt'])
                        for i in types["Cash Pic"]:
                            if i:
                                tab4.image(i)
                        tab4.write(types['Bank Pmt'])
                        for i in types["Bank Pic"]:
                            if i:
                                tab4.image(i)
                        if types["Others Pmt"]:
                            tab4.write(types['Others Pmt'])
                            for i in types["Others Pic"]:
                                if i:
                                    tab4.image(i)
        
                    
                    with tab0:
                        html_temp = """<div class='tableauPlaceholder' id='viz1667242170777' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ps&#47;pspstudy&#47;start&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='pspstudy&#47;start' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ps&#47;pspstudy&#47;start&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1667242170777');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='1900px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
                        html(html_temp, width=1200, height=1200, scrolling=True)
                    
                    
                    
                    # tab0.code(html_temp)
                    

