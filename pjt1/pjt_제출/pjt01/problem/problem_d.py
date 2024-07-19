# TMDB API 키 설정
# API_KEY = 'YOUR_API_KEY'
# BASE_URL = ''

# 문제 a에서 생성된 movies.csv 파일을 기반으로 영화 ID 목록 가져오기

# API 호출 함수

# 배우 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장

import requests
import csv
from pprint import pprint

BASE_URL = 'https://api.themoviedb.org/3/movie/'
API_KEY = '7a37661b2e2794690fcc8488efaba616'

def TMDB_API(movie_id) :
    url = f'{BASE_URL}{movie_id}/credits?api_key={API_KEY}'
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

def cast_data(movie) :
    cast_id = movie.get('id')
    #movie_id = movie
    name = movie.get('name').replace("\r\n"," ")
    character = movie.get('character').replace("\r\n"," ")
    order = movie.get('order')
    return [cast_id, movie_id, name, character, order]


movie_cast_list = []
movie_ids = read_movie_ids('movies.csv')
#print(movie_ids)

for movie_id in movie_ids :
    for item in TMDB_API(movie_id)['cast'] :
        #print(item)
        movie_cast_data = cast_data(item)
        #pprint(movie_cast_data)
        # if movie_cast_data[3] in movie_cast_list[:][3] :
        #     pass
        if movie_cast_data[3] == "" :
            movie_cast_data[3] =="이름 없음"
        if movie_cast_data[4] <= 10 :
            movie_cast_list.append(movie_cast_data)
    #pprint(movie_cast_list[:][3])

with open('movie_cast.csv', 'w',newline='',encoding='utf-8') as file :
    result = csv.writer(file)
    result.writerow(['cast_id','movie_id', 'name', 'character', 'order'])
    result.writerows(movie_cast_list)

