import pandas as pd
import json

# Cargar el archivo .json

with open("taylor_swift_spotify.json", "r") as j:
    data = json.load(j)


# Normalizar el archivo Json
    
df = pd.json_normalize(data, record_path=['albums', 'tracks'], 
                      meta=['artist_id', 'artist_name', 'artist_popularity',
                            ['albums', 'album_id'], ['albums', 'album_name'], ['albums', 'album_release_date'], 
                            ['albums', 'album_total_tracks']])


# Guardar el DataFrame en un archivo CSV
df.to_csv('dataset.csv', index=False)
