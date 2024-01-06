# Importar las librerias necesarias

import pandas as pd

# Leer el archivo CSV convertido

datos = pd.read_csv('dataset.csv')

# Analisis de datos faltantes:

# Para cada variable se va a contar el número de datos faltantes y posterior a ello se va a calcular una medida
# que permita ver el porcentaje de datos completos, teniendo en cuenta el número de filas del dataset. 

print("El número de filas es:", datos.shape[0])

# Identificamos el número de missing values en cada columna
p = datos.isnull().sum() 

# Porcentaje de datos completos en cada variable

porc_datos_completos = ( (datos.shape[0] - datos.isnull().sum()) / datos.shape[0]) * 100

print(porc_datos_completos)


# Ver valores duplicados 

duplicados = datos.duplicated(keep=False)

if duplicados.any():
    print("Se encontraron filas duplicadas.")
    print(datos[duplicados])
else:
    print("No hay filas duplicadas.")

#Validar datos duplicados por la columna track_id

duplicados_track_id = datos.duplicated(subset='track_id', keep=False)

if duplicados_track_id.any():
    print("Se encontraron valores duplicados.")
    print(datos[duplicados_track_id])
else:
    print("No hay valores duplicados.")    


# Verificar que el tipo de datos corresponda a lo que se tiene en la documentación

tipos_de_datos = datos.dtypes
print(tipos_de_datos)

# Una vez identificadas las variables que no tienen el tipo que corresponde según la documentación se procede 
# a realizar un analisis de valores unicos

# Variable explicit
niveles_explicit = datos['explicit'].unique()
print(niveles_explicit)

# Variable audio_features.key
niveles_audio_features_key = datos['audio_features.key'].unique()
print(niveles_audio_features_key)

# Variable audio_features.instrumentalness
niveles_audio_features_instrumentalness = datos['audio_features.instrumentalness'].unique()
print(niveles_audio_features_instrumentalness)

# Variable audio_features.time_signature
niveles_audio_features_time_signature = datos['audio_features.time_signature'].unique()
print(niveles_audio_features_time_signature)

# Variable album_release_date
niveles_album_release_date = datos['albums.album_release_date'].unique()
print(niveles_album_release_date)

# Variable album_total_tracks
niveles_album_total_tracks = datos['albums.album_total_tracks'].unique()
print(niveles_album_total_tracks)


# Evaluar los rangos de las variables númericas

# Tener en cuenta solo las columnas numericas
columnas_numericas = datos.select_dtypes(include=['int64', 'float64'])

# Calcular el max y el minimo de cada columna
maximos = columnas_numericas.max()
minimos = columnas_numericas.min()

print("Máximos por columna:")
print(maximos)

print("Mínimos por columna:")
print(minimos)



