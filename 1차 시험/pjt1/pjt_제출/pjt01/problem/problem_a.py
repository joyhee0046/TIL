# TMDB API 키 설정
# API_KEY = '7a37661b2e2794690fcc8488efaba616'
# BASE_URL = 'https://api.themoviedb.org/3/movie/'

# # API 호출 함수
# import requests
# response = requests.get(BASE_URL).json()
# print(response)
# 영화 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장


# TMDB API 키 설정
# API 호출 함수
import requests
BASE_URL = "https://api.themoviedb.org/3/discover/movie"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YTM3NjYxYjJlMjc5NDY5MGZjYzg0ODhlZmFiYTYxNiIsIm5iZiI6MTcyMTM1NTM5My4xMzk0MTEsInN1YiI6IjY2OTljOTIwYzQ2YzU4MDFhYmIxOTUxMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JC6JKgP1Yq0yahC0IPuL1upnNebYseX3BIaSdHtpKnE"
}
response = requests.get(BASE_URL, headers=headers).json()
#print(response)

movies = []
fields = ['id', 'title', 'release_date', 'popularity']
for item in response['results']:
    temp_dict = {}
    for key in fields:
        temp_dict[key] = item[key]
        #print(temp_dict)
    movies.append(temp_dict)
#print(movies)

import csv
with open('movies.csv', 'w', newline='', encoding='utf-8') as file:
    fieldsname = ['id', 'title', 'release_date', 'popularity']
    content = csv.DictWriter(file, fieldnames=fieldsname)
    content.writeheader()
    for item in movies:
        #print(item)
        content.writerow(item)