import requests
import csv

BASE_URL = 'https://api.themoviedb.org/3/movie/'
API_KEY = '7a37661b2e2794690fcc8488efaba616'

def TMDB_API(movie_id) :
    url = f'{BASE_URL}{movie_id}?api_key={API_KEY}'
    response = requests.get(url)
    response.raise_for_status()   #오류발생시에 예외처리
    return response.json()

def read_movie_ids(file_path) :
    movie_ids = []
    with open(file_path, 'r', encoding='utf-8') as file :
        result = csv.DictReader(file)
        for row in result :
            movie_ids.append(row['id'])
    return movie_ids

def process_movie_data(movie) :
    movie_id = movie['id']
    budget = movie.get('budget',0)
    revenue = movie.get('revenue',0)
    runtime = movie.get('runtime',0)
    genres = ', '.join([genres['name']for genres in movie.get('genres',[])])
    return [movie_id, budget, revenue, runtime, genres]


movie_details_list = []
movie_ids = read_movie_ids('movies.csv')
#print(movie_ids)

for movie_id in movie_ids :
    data = TMDB_API(movie_id)
    #print(data)
    processed_movie = process_movie_data(data)
    #print(processed_movie)
    movie_details_list.append(processed_movie)

with open('movie_datails_t.csv', 'w',newline='',encoding='utf-8') as file :
    result = csv.writer(file)
    result.writerow(['movie_id', 'budget', 'revenue', 'runtime', 'genres'])
    result.writerows(movie_details_list)


