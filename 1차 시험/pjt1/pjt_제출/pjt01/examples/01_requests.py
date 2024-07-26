# from 모듈 import 함수
# from 패키지 import 모듈
# from 패키지.모듈 import 함수
import requests
from pprint import pprint

URL = 'https://jsonplaceholder.typicode.com/todos/'
response = requests.get(URL).json()
# response = requests.post(URL).json()
# response = requests.delete(URL).json()
print(response)
# print(type(response))

# 내 서비스에 필요한 정보만 모아 놓은 리스트
completed_todo = []
# 내 서비스에 필요로 하는 필드 명
fields = ['id', 'title']
for item in response:
    # completed가 True인 경우만
    if item['completed']:
        # 모든 item을 순회하면서, 
        # 새 리스트 completed_todo에 넣어야 될
        # 내 서비스에 필요한 필드만 가진 새로운 dict
        temp_dict = {}
        for key in fields:
            # 전처리한 item이 가진 정보를 토대로.. 작성자 정보를 추가
            temp_dict[key] = item[key]
            # print(temp_dict)
        completed_todo.append(temp_dict)

pprint(completed_todo)