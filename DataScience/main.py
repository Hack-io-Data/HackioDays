
# Librerías numéricas
# -----------------------------------------------------------------------
import pandas as pd  
#import pandas_profiling
from pydantic.v1 import BaseSettings


pd.pandas.set_option('display.max_columns', None)

import sweetviz as sv
# Librerías de streamlit
# -----------------------------------------------------------------------
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

# configurar el diseño de la página para que el contenido se ajuste al ancho del navegador
st.set_page_config(layout="wide")

# insertamos una imagen 
#sst.image("Imagenes/logo_celeste@4x.png")

# creamos un input para que el usuario inserte el conjunto de datos que sea
fichero = st.file_uploader("Choose a CSV file", accept_multiple_files=False)


# mientras que el archivo no haya sido subido por el usuario, no se ejecutará el cádigo que tenemos a continuación
if fichero is not None:
    st.markdown("### Pandas Profiling Report")

    # convertimos el csv que inserta el usuario a daaframe
    df = pd.read_csv(fichero)

    # mostramos dos filas aleatorias del dataframe
    st.table(df.sample(2))

    #pr = df.profile_report()
    #pst_profile_report(pr)
