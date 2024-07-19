# requests : is a simple, yet elegant, HTTP library.
# $ pip install requests

'''
모듈 부르기.
import M  #모듈에 들어있는 다양한 함수를 사용할거임
from M import F   #F함수 하나만 사용할거임
from P import M   
from P.M import F
'''

#더미정보 사이트 https://jsonplaceholder.typicode.com/

import requests
from pprint import pprint 

URL = 'https://jsonplaceholder.typicode.com/todos/'
# response = requests.get(URL)      #프린트 찍으면 <Response [200]>으로 나옴. 잘 불러졌다는 의미
response = requests.get(URL).json()    #프린트 찍으면 내용 확인 가능. json형태 파일이라고 미리 설정해줬으니까
# print(response)
# print(type(response))    #list타입으로 형변환 완료임을 확인.

# 조건에 맞는 정보를 원하는 컬럼으로 새로 정리.
completed_todo = []
fields = ['id','title']
for item in response :
    if item['completed'] == True :
        temp_dict = {}
        for key in fields:
            temp_dict[key]= item[key]
            #print(temp_dict)
        completed_todo.append(temp_dict)

# print(completed_todo)
pprint(completed_todo)