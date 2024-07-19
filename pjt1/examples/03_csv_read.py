import csv

with open('users.csv', 'r', encoding='utf-8') as file :
    #content = csv.reader(file)    # 바로 사용 가능한 리스트 형태로 생성.
    content = csv.DictReader(file)   # 첫행을 컬럼으로 설정하여 딕셔너리 형태로 생성.
    print(content)
    for row in content :
        print(row)

