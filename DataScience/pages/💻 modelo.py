
# Librerías numéricas
# -----------------------------------------------------------------------
import pandas as pd  


pd.pandas.set_option('display.max_columns', None)


# Librerías de streamlit
# -----------------------------------------------------------------------
import streamlit as st


# configurar el diseño de la página para que el contenido se ajuste al ancho del navegador
st.set_page_config(layout="wide")

# insertamos una imagen 
#st.image("../Imagenes/logo_celeste@4x.png")

# creamos un input para que el usuario inserte el conjunto de datos que sea
fichero = st.file_uploader("Choose a CSV file", accept_multiple_files=False)


# mientras que el archivo no haya sido subido por el usuario, no se ejecutará el cádigo que tenemos a continuación
if fichero is not None:
    # convertimos el csv que inserta el usuario a daaframe
    df = pd.read_csv(fichero)

    # mostramos dos filas aleatorias del dataframe
    st.table(df.sample(2))

    # import ClusteringExperiment and init the class
    from pycaret.clustering import ClusteringExperiment
    from pycaret.clustering import *
    exp_clu101 = setup(df, normalize = True, 
                   ignore_features = [],
                   session_id = 123)
    kmeans = create_model('kmeans')
    kmean_results = assign_model(kmeans)

    st.table(kmean_results.head(1))
    text_contents = '''This is some text'''
    st.download_button("Download some text", kmean_results.to_csv(index = False))