
import pandas as pd

# 1. Cargar archivo original
df = pd.read_csv("data/datos_latam.csv")
print("Datos cargados:", df.shape)

# 2. Eliminar filas vacías
df.dropna(inplace=True)

# 3. Extraer año de la columna de fecha
df['Año'] = pd.to_datetime(df['date']).dt.year

# 4. Eliminar columna 'date' si no se va a usar
df.drop(columns=['date'], inplace=True)

# 5. Reordenar columnas
columnas = ['country', 'Año', 'PIB_USD', 'Inflacion_Porcentaje', 'Tipo_Cambio_USD', 'Crecimiento_PIB_Porcentaje', 'Poblacion_Total']
df = df[columnas]

# 6. Guardar nuevo archivo limpio
df.to_csv("data/datos_latam_limpios.csv", index=False)
print("Archivo limpio guardado en 'data/datos_latam_limpios.csv'")
