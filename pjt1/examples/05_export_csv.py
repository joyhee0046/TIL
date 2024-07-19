import requests
from pprint import pprint 
import csv

URL = 'https://jsonplaceholder.typicode.com/todos/'
response = requests.get(URL).json() 
completed_todo = []
fields = ['id','title']
for item in response :
    if item['completed'] == True :
        temp_dict = {}
        for key in fields:
            temp_dict[key]= item[key]
        completed_todo.append(temp_dict)

#pprint(completed_todo)

with open('compledtet_todos.csv', 'w', newline='', encoding='utf-8') as file:
    fieldsname = ['id', 'title']
    content = csv.DictWriter(file, fieldnames=fieldsname)

    content.writeheader()

    for item in completed_todo:
        #print(item)
        content.writerow(item)
 # 조건에 맞는 딕셔너리 92행 생성 완료.