
# Librerías numéricas
# -----------------------------------------------------------------------
import pandas as pd  


pd.pandas.set_option('display.max_columns', None)

# Librerías de streamlit
# -----------------------------------------------------------------------
import streamlit as st

import os
# configurar el diseño de la página para que el contenido se ajuste al ancho del navegador
st.set_page_config(layout="wide")


dir_name = os.path.abspath(os.path.dirname(__file__))
print(dir_name)

st.markdown("<h1 style='text-align: center;color: #49F2D3;'>⌗ Hackio Data Science Challenge ⌗</h1>", unsafe_allow_html=True)

# insertamos una imagen 
#st.image("Imagenes/logo_celeste@4x.png")
st.markdown("<h1 style='text-align: left;color: #49F2D3;'> Datos</h1>", unsafe_allow_html=True)
st.write("El conjunto de datos captura varias métricas relacionadas con la interacción del cliente con la compañía de seguros. Esto incluye el valor del tiempo de vida del cliente, que mide cuánto valor aporta el cliente a la empresa durante su relación, y la respuesta a ofertas de marketing. También se registra el número de reclamaciones presentadas y el monto total de estas reclamaciones, así como el número de quejas abiertas, lo cual puede ser un indicador de la satisfacción del cliente." )
st.write("Además de los detalles personales y de la póliza, el conjunto de datos proporciona información sobre los vehículos asegurados. Esto incluye la clase del vehículo (como sedán de cuatro puertas, SUV, etc.) y el tamaño del vehículo. Estos datos son útiles para analizar cómo diferentes tipos de vehículos pueden influir en la elección del seguro y en el comportamiento del cliente.")
# abrimos el csv con el que vamos a trabajar
df = pd.read_csv("Datos/Customers.csv")
st.table(df.head())


col1, col2 = st.columns(2)
with col1: 
    st.markdown("""
            | **Columna**                    | **Descripción**                                                                     |
            |--------------------------------|-------------------------------------------------------------------------------------|
            | `Customer`                     | ID del cliente, un identificador único para cada cliente.                           |
            | `State`                        | Estado de residencia del cliente.                                                   |
            | `Customer Lifetime Value`      | Valor del tiempo de vida del cliente.                                               |
            | `Response`                     | Respuesta del cliente a una oferta de marketing (Sí/No).                            |
            | `Coverage`                     | Tipo de cobertura de seguro (Básico, Extendido, Premium).                           |
            | `Education`                    | Nivel educativo del cliente (e.g., Bachillerato, Licenciatura, etc.).               |
            | `Effective To Date`            | Fecha de efectividad de la póliza de seguro.                                        |
            | `Employment Status`            | Estado laboral del cliente (Empleado, Desempleado, etc.).                           |
            | `Gender`                       | Género del cliente (F/M).                                                           |
            | `Income`                       | Ingreso anual del cliente.                                                          |
            | `Location Code`                | Código de ubicación del cliente (e.g., Suburbano, Rural).                           |
            | `Marital Status`               | Estado civil del cliente (Casado, Soltero).                                         |
            | `Monthly Premium Auto`         | Prima mensual del seguro de automóvil.                                              |
        """)
with col2:
    st.markdown("""
            | **Columna**                    | **Descripción**                                                                     |
            |--------------------------------|-------------------------------------------------------------------------------------|
            | `Months Since Last Claim`      | Meses desde la última reclamación de seguro del cliente.                            |
            | `Months Since Policy Inception`| Meses desde el inicio de la póliza del cliente.                                     |
            | `Number of Open Complaints`    | Número de quejas abiertas que tiene el cliente.                                     |
            | `Number of Policies`           | Número de pólizas de seguro que tiene el cliente.                                   |
            | `Policy Type`                  | Tipo de póliza (e.g., Personal Auto, Corporate Auto).                               |
            | `Policy`                       | Detalles específicos de la póliza (e.g., Personal L1, Corporate L3).                 |
            | `Renew Offer Type`             | Tipo de oferta de renovación ofrecida al cliente (e.g., Offer1, Offer2).            |
            | `Sales Channel`                | Canal de ventas a través del cual el cliente adquirió el seguro (e.g., Agente, Centro de Llamadas). |
            | `Total Claim Amount`           | Monto total de las reclamaciones del cliente.                                       |
            | `Vehicle Class`                | Clase del vehículo del cliente (e.g., Two-Door Car, SUV).                          |
            | `Vehicle Size`                 | Tamaño del vehículo del cliente (e.g., Medsize).                                    |
            """)

st.markdown("<h1 style='text-align: left;color: #49F2D3;'>Objetivo</h1>", unsafe_allow_html=True)
st.markdown("""

            1. **Carga y Preprocesamiento de Datos**
                - Importar y cargar el conjunto de datos de clientes.
                - Limpiar los datos para manejar valores nulos, duplicados e inconsistencias.
                - Seleccionar las características relevantes para la segmentación.
                - Normalizar o estandarizar los datos para asegurar una contribución equitativa de todas las características.

            2. **Análisis Exploratorio de Datos (EDA)**
                - Realizar un análisis descriptivo para entender la distribución de las características.
                - Visualizar las relaciones entre diferentes variables utilizando gráficos como histogramas, diagramas de dispersión y gráficos de caja.
                - Identificar posibles patrones o grupos preliminares en los datos.

            3. **Segmentación de Clientes utilizando Clustering**
                - Aplicar técnicas de clustering, como K-Means, para agrupar a los clientes en diferentes segmentos.
                - Determinar el número óptimo de clusters utilizando métodos como el método del codo (elbow method) o el coeficiente de silueta.
                - Visualizar los clusters en un espacio reducido de dimensiones usando PCA o t-SNE.

            4. **Evaluación de la Segmentación**
                - Evaluar la calidad de los clusters utilizando métricas como el coeficiente de silueta, el índice de Davies-Bouldin y el índice de Calinski-Harabasz.
                - Interpretar los resultados de la segmentación describiendo las características distintivas de cada cluster.
                - Comparar los perfiles de los clientes en cada segmento para identificar diferencias y similitudes clave.

            5. **Desarrollo de Estrategias Comerciales**
                - Proponer estrategias comerciales específicas para cada segmento basado en el análisis realizado.
                - Considerar diferentes aspectos como ofertas de productos, estrategias de marketing, canales de comunicación y servicios personalizados.
                - Justificar cada estrategia con datos y análisis obtenidos del clustering.

            6. **Presentación de Resultados**
                - Preparar una presentación que resuma el análisis realizado, los resultados de la segmentación y las estrategias comerciales propuestas.
                - Incluir visualizaciones que ayuden a ilustrar los perfiles de los segmentos y las recomendaciones estratégicas.
                - Presentar las conclusiones y responder preguntas o comentarios sobre el análisis y las estrategias.

            #### Entregables del Proyecto

            1. **Informe de Segmentación y Evaluación**
                - Un informe detallado que incluya el análisis exploratorio, la metodología de clustering, la evaluación de los clusters y la interpretación de los resultados.
                - Descripción de las estrategias comerciales propuestas para cada segmento.

            3. **Presentación**
                - Una presentación en formato PowerPoint o PDF que resuma los principales hallazgos y estrategias del proyecto.
                - Visualizaciones y gráficos que ayuden a comunicar los resultados de manera efectiva.
""")
