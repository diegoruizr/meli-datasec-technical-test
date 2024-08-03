import requests

def bestInGenre(genre):
    best_show = None
    page = 1
    genre = genre.lower().strip()
    best_rating = float('-inf')

    while True:
        url = f'https://jsonmock.hackerrank.com/api/tvseries?page={page}'
        response = requests.get(url)
        
        if response.status_code != 200:
            break

        data = response.json()
        shows = data['data']

        if not shows:
            break

        for show in shows:
            show_genres = [g.strip().lower() for g in show['genre'].split(',')]
            if genre in show_genres:
                show_rating = float(show['imdb_rating'])
                if best_show is None or show_rating > best_rating or (show_rating == best_rating and show['name'] > best_show['name']):
                    best_show = show
                    best_rating = show_rating

        page += 1

    return best_show['name'] if best_show else f'No se encontraron series con el genero {genre}, o existe error al consultar la URL externa'

if __name__ == "__main__":
    genre = input("Ingrese el género de la serie: ").strip()
    print(bestInGenre(genre))