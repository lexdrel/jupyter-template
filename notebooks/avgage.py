import pandas as pd
import random
import secrets

random.seed(42)

n = 100

genres = [
    'Rock','Pop','Jazz','Hip Hop','Reggaeton','Salsa','Bachata','Cumbia','Metal','Electronic',
    'House','Techno','Classical','Country','Blues','Funk','R&B','Indie','K-Pop','Latin'
]

first_names = ['Luna','Marco','Sofia','Diego','Valeria','Mateo','Camila','Bruno','Alma','Nico',
               'Iris','Gael','Mia','Leo','Renata','Pablo','Dalia','Hugo','Vera','Ivan']
last_names  = ['Ramirez','Ortega','Silva','Navarro','Vega','Castillo','Mendoza','Rios','Santos',
               'Paredes','Lozano','Cruz','Reyes','Herrera','Flores','Naranjo','Delgado','Serrano',
               'Ibarra','Quintero']

track_words = ['Noche','Luz','Corazon','Camino','Fuego','Mar','Viento','Ciudad','Sombra','Tiempo',
               'Destino','Cielo','Arena','Sueno','Ritmo','Voz','Mirada','Latido','Viaje','Eco']

rows = []
for _ in range(n):
    user_id = secrets.token_hex(4).upper()      # 8 hex chars
    total_play = round(random.uniform(0, 500), 4)
    artist = f"{random.choice(first_names)} {random.choice(last_names)}"
    genre = random.choice(genres)
    track = " ".join(random.choice(track_words) for _ in range(4))  # 4 words
    rows.append((user_id, total_play, artist, genre, track))

df = pd.DataFrame(rows, columns=['user_id','total_play','artist','genre','track'])
df.to_csv('music_sample_100.csv', index=False)