
# Librerías numéricas
# -----------------------------------------------------------------------
import pandas as pd  


pd.pandas.set_option('display.max_columns', None)

# import ClusteringExperiment and init the class
from pycaret.clustering import ClusteringExperiment
from pycaret.clustering import *

# Librerías de streamlit
# -----------------------------------------------------------------------
import streamlit as st

# configurar el diseño de la página para que el contenido se ajuste al ancho del navegador
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: #F2C349; font-size: 100px;'>⌗ Hackio Data Science Challenge ⌗</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left;color: #49F2D3;'> Customer Segmentation Challenge</h1>", unsafe_allow_html=True)


# Descripción de la aplicación
st.markdown("""
Los pasos que deberéis seguir son: 

1. **Preprocersar los datos**: Utilizad las herramientas de limpieza  y preparación de datos que has aprendido.
            
2. **Sube el archivo CSV**: Subid el archivo con los datos preprocesados.
            
3. **Segmentación de clientes**: Vuestro archivo pasará por un modelo de segmentación de clientes que asignará cada registro a un clúster.
            
4. **Descargar los resultados**: Obtened un archivo CSV con una nueva columna que contiene la información de los clústeres.
            
5. **Analizar los clústeres**: Utilizad gráficos para interpretar y presentar los resultados de la segmentación.

### Instrucciones:
            
1. Asegúrate de que tu archivo CSV está correctamente formateado.
            
2. Sube el archivo utilizando el botón de carga.
            
3. Descarga el archivo procesado con la columna de clústeres añadida.
            
4. Utiliza herramientas de visualización para analizar los clústeres y generar extraer las conclusiones necesarias.

""")

# insertamos una imagen 
#st.image("../Imagenes/logo_celeste@4x.png")

# creamos un input para que el usuario inserte el conjunto de datos que sea
fichero = st.file_uploader("Sube el archivo csv", accept_multiple_files=False)


# mientras que el archivo no haya sido subido por el usuario, no se ejecutará el cádigo que tenemos a continuación
if fichero is not None:
    # convertimos el csv que inserta el usuario a daaframe
    df = pd.read_csv(fichero, sep = ";")
    st.markdown("<h1 style='text-align: left;color: #49F2D3;'> Vuestros datos para el Cluster</h1>", unsafe_allow_html=True)
    st.markdown("> #### Muestra de datos")

    # mostramos dos filas aleatorias del dataframe
    st.table(df.sample(5))


    exp_clu101 = setup(df, normalize = True, 
                   ignore_features = [],
                   session_id = 123)
    kmeans = create_model('kmeans')
    kmean_results = assign_model(kmeans)


    st.markdown("<h1 style='text-align: left;color: #49F2D3;'> Los resultados</h1>", unsafe_allow_html=True)
    st.markdown("> #### Muestra de resultados")

    st.table(kmean_results.sample(5))
    st.download_button("Descarga el conjunto de datos con los clusters", kmean_results.to_csv(index = False))