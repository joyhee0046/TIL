# 아래에 코드를 작성하시오.

movies = ['Inception','Interstellar','Dunkirk','Tenet']

def get_movie_recommendation(rating) :
    if rating >= 9 :
        return 'Inception'
    elif rating >= 8 :
        return 'Interstellar'
    elif rating >= 7 :
        return 'Dunkirk'
    else : 
        return 'Tenet'

score = int(input("Enter your movie rating (0-10): "))
print(f"Recommended movie: {get_movie_recommendation(score)}")