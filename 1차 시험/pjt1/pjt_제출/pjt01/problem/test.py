import requests

def get_genre():
    base_url = 'https://api.themoviedb.org/3'
    path = '/genre/movie/list'

    params = {
        'api_key' : '7a37661b2e2794690fcc8488efaba616',
        'language' : 'ko',
    }
    res_genre = requests.get(base_url + path, params=params)
    genre_list = res_genre.json()
    return genre_list
print(get_genre())

def get_pop():

    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'

    params = {
        'api_key' : '7a37661b2e2794690fcc8488efaba616',
        'language' : 'ko',
    }
    res = requests.get(base_url+path, params=params)
    data = res.json()
    # return(data)
    result = data['results']
    
    janre_list = get_genre()
    for i in result:
        for j in range(len(i['genre_ids'])):
            for p in janre_list['genres']:
                if i['genre_ids'][j] == p.get('id'):
                    i['genre_ids'][j] = p.get('name')
        i['genre_ids'] = i['genre_ids'][0]       
    return result

print(get_pop())