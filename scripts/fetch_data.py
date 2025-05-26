
import wbdata
import pandas as pd
import datetime

# Indicadores y nombres más amigables
indicators = {
    'NY.GDP.MKTP.CD': 'PIB_USD',
    'FP.CPI.TOTL.ZG': 'Inflacion_Porcentaje',
    'PA.NUS.FCRF': 'Tipo_Cambio_USD',
    'NY.GDP.MKTP.KD.ZG': 'Crecimiento_PIB_Porcentaje',
    'SP.POP.TOTL': 'Poblacion_Total'
}

# Países seleccionados
countries = ['ARG', 'BOL', 'BRA', 'CHL', 'COL', 'CRI', 'CUB', 'DOM',
             'ECU', 'GTM', 'HND', 'MEX', 'NIC', 'PAN', 'PAR', 'PER',
             'SLV', 'URY', 'VEN']

# Rango de fechas
data_date = (datetime.datetime(2010, 1, 1), datetime.datetime(2023, 12, 31))

# Descargar datos
df = wbdata.get_dataframe(indicators, country=countries, data_date=data_date, convert_date=True)
df.reset_index(inplace=True)
df.to_csv("data/datos_latam.csv", index=False)
print("Datos guardados correctamente.")
