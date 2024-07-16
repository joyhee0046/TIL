# 아래에 코드를 작성하시오.

movies = ['Inception','Interstellar','Dunkirk','Tenet']
score = [9,8.5,7.5,6]

# new_movies_list=[]
# for tt, rt in zip(movies, ratings) :  ##zip은 튜플로 묶어줌._짝이 없는 친구는 버림.오류가능성 감소
#     temp_dict = {'title': tt, 'rating': rt}
#     new_movies_list.append(temp_dict)

#comp_movies = [{'title': tt, 'rating': rt} for tt, rt in zip(movies, ratings)]

movie_dict=[]
for i in range(len(movies)) :
    movie_dict.append({"title" : movies[i] , "rating": score[i]})
print(movie_dict)

def get_high_rated_movies(threshold) :
    recommend_li = []
    for i in range(len(movies)) :
        # if score[i] >= threshold :
        #     recommend_li.append(movies[i])
        if movie_dict[i]["rating"] >= threshold :
            recommend_li.append(movie_dict[i]["title"])
    return recommend_li

threshold = int(input("Enter the rating threshold: "))
#high_rated_movies = get_high_rated_movies(threshold)
# for movie in high_rated_movies :
#     print(movie)
print(f"Movies with a rating of {threshold:.1f} or higher :")
print(*get_high_rated_movies(threshold), sep = "\n")