import csv

# newline을 지정하지 않은 경우
with open('data.csv', 'w', encoding='utf-8') as file:
    content = csv.writer(file)
    content.writerow(['이름', '나이', '직업'])
    content.writerow(['홍길동', '30', '개발자'])
    content.writerow(['김철수', '25', '디자이너'])
    content.writerow(['이영희', '28', '기획자'])

# newline을 '' 으로 지정
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    content = csv.writer(file)
    content.writerow(['이름', '나이', '직업'])
    content.writerow(['홍길동', '30', '개발자'])
    content.writerow(['김철수', '25', '디자이너'])
    content.writerow(['이영희', '28', '기획자'])

# DictWriter
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    # 지정해주면 좋은 내용으로...
    # fieldsname
    fieldsname = ['이름', '나이', '직업']
    content = csv.DictWriter(file, fieldnames=fieldsname)

    content.writeheader()
    # content.writerow({'이름': '이름', '나이': '나이', '직업': '직업'})
    content.writerow({'이름': '홍길동', '나이': '30', '직업': '개발자'})
    content.writerow({'나이': '25', '이름': '김철수', '직업': '디자이너'})
    content.writerow({'직업': '기획자', '이름': '이영희', '나이': '28'})