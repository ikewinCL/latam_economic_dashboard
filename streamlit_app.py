
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("data/datos_latam_limpios.csv")

# Título y descripción
st.title("📊 Dashboard Económico de América Latina")
st.markdown("Visualización interactiva de indicadores económicos entre 2010 y 2023.")

# Filtros
paises = df['country'].unique()
indicadores = ['PIB_USD', 'Inflacion_Porcentaje', 'Tipo_Cambio_USD', 'Crecimiento_PIB_Porcentaje']

pais = st.selectbox("Selecciona un país", paises)
indicador = st.selectbox("Selecciona un indicador", indicadores)

df_filtrado = df[df['country'] == pais]

fig = px.line(df_filtrado, x='Año', y=indicador, title=f"{indicador} en {pais}")
st.plotly_chart(fig)
