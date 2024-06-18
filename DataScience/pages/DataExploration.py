
# Librerías numéricas
# -----------------------------------------------------------------------
import pandas as pd  


pd.pandas.set_option('display.max_columns', None)

# Librerías de streamlit
# -----------------------------------------------------------------------
import streamlit as st
import streamlit.components.v1 as components


import sweetviz as sv

import os

# configurar el diseño de la página para que el contenido se ajuste al ancho del navegador
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: #F2C349; font-size: 100px;'>⌗ Hackio Data Science Challenge ⌗</h1>", unsafe_allow_html=True)

dir_name = os.path.abspath(os.path.dirname(__file__))

st.markdown("<h1 style='text-align: left;color: #49F2D3;'> Datos</h1>", unsafe_allow_html=True)
st.write("El conjunto de datos captura varias métricas relacionadas con la interacción del cliente con la compañía de seguros. Esto incluye el valor del tiempo de vida del cliente, que mide cuánto valor aporta el cliente a la empresa durante su relación, y la respuesta a ofertas de marketing. También se registra el número de reclamaciones presentadas y el monto total de estas reclamaciones, así como el número de quejas abiertas, lo cual puede ser un indicador de la satisfacción del cliente." )
st.write("Además de los detalles personales y de la póliza, el conjunto de datos proporciona información sobre los vehículos asegurados. Esto incluye la clase del vehículo (como sedán de cuatro puertas, SUV, etc.) y el tamaño del vehículo. Estos datos son útiles para analizar cómo diferentes tipos de vehículos pueden influir en la elección del seguro y en el comportamiento del cliente.")

# join the bobrza1.csv to directory to get file path
location = os.path.join(dir_name, 'Customers.csv')
st.markdown("> #### Muestra de datos")
df = pd.read_csv(location)
st.table(df.head())

st.markdown("<h1 style='text-align: left;color: #49F2D3;'> Exploración de los Datos</h1>", unsafe_allow_html=True)

my_report = sv.analyze(df, feat_cfg=sv.FeatureConfig(
        force_text=[]), target_feat=None)
my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"

html_file = "output.html"
# analysis.show_html(html_file)
# Get the current directory
current_dir = os.getcwd()
# Create the full path to the HTML file
full_path = os.path.join(current_dir, html_file)

# Render the output on a web page.
my_report.show_html(filepath=full_path, open_browser=False, layout='vertical', scale=1.0)
HtmlFile = open("output.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=1000, width=1350, scrolling=True)
# components.iframe(src='http://localhost:3001/EDA.html', width=1100, height=1200, scrolling=True)


