from flask import Flask, request
import requests

app = Flask(__name__)

# Ruta de ejemplo para obtener datos
@app.route('/api/shows', methods=['GET'])
def bestInGenre():
     # Obtener el parámetro de consulta 'page' y 'genre' de la URL
    page = request.args.get('page', default=1, type=int)
    genre = request.args.get('genre', default='', type=str)

     # URL de la API externa con el parámetro de página
    url = f'https://jsonmock.hackerrank.com/api/tvseries?page={page}'

    # Hacer la solicitud a la API externa
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        shows = data['data']
        
        # Filtrar las series por género
        filtered_shows = [show for show in shows if genre.lower() in [g.strip().lower() for g in show['genre'].split(',')]]
        
        # Encontrar la serie con la calificación imdb_rating más alta
        if filtered_shows:
            best_show = max(filtered_shows, key=sort_key)
            result = best_show['name']
        else:
            result =  f'No se encontraron series con el genero {genre}'
    else:
        result = 'Error al obtener datos de la API externa'
    
    return result

def sort_key(show):
    return float(show['imdb_rating']), show['name']

if __name__ == '__main__':
    app.run(debug=True)