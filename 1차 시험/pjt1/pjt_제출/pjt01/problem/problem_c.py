# # TMDB API 키 설정
# API_KEY = 'YOUR_API_KEY'
# BASE_URL = ''

# 영화 ID 리스트를 movies.csv 파일에서 읽어옴

# API 호출 함수

# 리뷰 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장

import requests
import csv
from pprint import pprint

BASE_URL = 'https://api.themoviedb.org/3/movie/'
API_KEY = '7a37661b2e2794690fcc8488efaba616'

def TMDB_API(movie_id) :
    url = f'{BASE_URL}{movie_id}/reviews?api_key={API_KEY}'
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

def review_data(movie) :
    review_id = movie.get('id')
    #movie_id = movie
    author = movie.get('author')
    content = movie.get('content').replace("\r\n","")
    rating = movie.get('author_details')
    return [review_id, movie_id, author, content, rating['rating']]


movie_review_list = []
movie_ids = read_movie_ids('movies.csv')
#print(movie_ids)

for movie_id in movie_ids :
    for item in TMDB_API(movie_id)['results'] :
        movie_review_data = review_data(item)
        #pprint(movie_review_data)
        if movie_review_data[3] == "" :
            movie_review_data[3] =="내용없음"
        if type(movie_review_data[4]) is float : 
            if movie_review_data[4] >= 5.0 :
                movie_review_list.append(movie_review_data)


with open('movie_reviews.csv', 'w',newline='',encoding='utf-8') as file :
    result = csv.writer(file)
    result.writerow(['review_id','movie_id', 'author', 'content', 'rating'])
    result.writerows(movie_review_list)



