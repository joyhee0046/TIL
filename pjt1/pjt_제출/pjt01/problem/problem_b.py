import requests, csv, pprint

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YTM3NjYxYjJlMjc5NDY5MGZjYzg0ODhlZmFiYTYxNiIsIm5iZiI6MTcyMTM1NTM5My4xMzk0MTEsInN1YiI6IjY2OTljOTIwYzQ2YzU4MDFhYmIxOTUxMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JC6JKgP1Yq0yahC0IPuL1upnNebYseX3BIaSdHtpKnE"
}

response=[]

with open('movies.csv', newline='') as csvfile:
    movies = csv.reader(csvfile)
    for row in movies:
        response.append(requests.get("https://api.themoviedb.org/3/movie/" + row[0] + "?language=ko-KR", headers=headers).json())
# pprint.pprint(response)

movie_details = []
fields = ['id', 'budget','revenue','runtime','genres']
for item in response[1:][:]:
    temp_dict = {}
    for key in fields:
        temp_dict[key] = item[key]
    movie_details.append(temp_dict)
#pprint.pprint(movie_details)

with open('movie_details.csv', 'w', newline='', encoding='utf-8') as file:
    fieldsname = ['id', 'budget','revenue','runtime','genres']
    content = csv.DictWriter(file, fieldnames=fieldsname)

    content.writeheader()

    for item in movie_details:
        print(item)
        content.writerow(item)