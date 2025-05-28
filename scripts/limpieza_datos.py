
import pandas as pd
import os

# Crear la carpeta 'data' si no existe
os.makedirs("data", exist_ok=True)

# Leer el archivo original
df = pd.read_csv("data/datos_latam.csv")

# Convertir los nombres de países en formato título
df["Pais"] = df["Pais"].str.title()

# Redondear decimales a 2 dígitos
df["PBI"] = df["PBI"].round(2)
df["Tasa_Inflacion"] = df["Tasa_Inflacion"].round(2)
df["Estabilidad_Macro"] = df["Estabilidad_Macro"].round(2)

# Guardar archivo limpio
df.to_csv("data/datos_latam_limpios.csv", index=False)

print("Archivo 'datos_latam_limpios.csv' creado correctamente.")
