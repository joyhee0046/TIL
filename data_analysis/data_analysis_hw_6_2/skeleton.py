# 포함 기술스택: python, pandas
import pandas as pd

# 데이터 로드
file_path = pd.read_csv("movie_data.csv")
# print(file_path)
movies = file_path

# 사용자로부터 감독 이름 입력 받기
director_name = input("감독의 이름을 입력하세요: ")

# 특정 감독의 영화 필터링
director_movies = movies[movies['Director'] == director_name]
# print(director_movies)

# 평균 평점 계산
average_rating = director_movies['Rating'].mean()
print(f"{director_name} 감독 영화의 평균 평점: {average_rating:.2f}")

# 가장 높은 평점을 받은 영화 찾기
best_movie = movies[movies['Rating'] == max(movies['Rating'])]
print(f"가장 높은 평점을 받은 영화: {best_movie['Title']} ({best_movie['Rating']})")