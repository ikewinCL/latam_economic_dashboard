
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("data/datos_latam_limpios.csv")
df['Año'] = df['Año'].astype(int)  # 👈 Corrige el eje X con enteros

# Ver columnas disponibles
st.write("Columnas disponibles:", df.columns.tolist())

# Título y descripción
st.title("📊 Dashboard Económico de América Latina")
st.markdown("Visualización interactiva de indicadores económicos entre 2010 y 2023.")

# Filtros
paises = df['Pais'].unique()
indicadores = ['PBI', 'Tasa_Inflacion', 'Tipo_Cambio', 'Estabilidad_Macro']

pais = st.selectbox("Selecciona un país", paises)
indicador = st.selectbox("Selecciona un indicador", indicadores)

df_filtrado = df[df['Pais'] == pais]

fig = px.line(df_filtrado, x='Año', y=indicador, title=f"{indicador} en {pais}")
st.plotly_chart(fig)


