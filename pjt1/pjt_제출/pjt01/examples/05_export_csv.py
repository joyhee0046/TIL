import requests
import csv
from pprint import pprint

URL = 'https://jsonplaceholder.typicode.com/todos/'
response = requests.get(URL).json()

completed_todo = []
fields = ['id', 'title']
for item in response:
    if item['completed']:
        temp_dict = {}
        for key in fields:
            temp_dict[key] = item[key]
        completed_todo.append(temp_dict)

with open('compledted_todos.csv', 'w', newline='', encoding='utf-8') as file:
    fieldsname = ['id', 'title']
    content = csv.DictWriter(file, fieldnames=fieldsname)

    content.writeheader()

    for item in completed_todo:
        # print(item)
        content.writerow(item)