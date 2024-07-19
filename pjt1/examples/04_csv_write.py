import csv
'''
newline 매개변수.
파일의 모든 줄바꿈문자를 기본 줄바꿈 문자로 변환처리.
'' : 줄바꿈 안해
'\n' : 줄바꿈을 LF로 변환
'\r\n' : 줄바꿈을 CRLF로 변환
'\r' : 줄바꿈을 CR로 변환
'''



# with open('data.csv', 'w', encoding='utf-8') as file :  #있는 파일을 열거나 없으면 생성
#     content = csv.writer(file)
#     content.writerow(['이름', '나이','직업'])   #한행씩 데이터 넣
#     content.writerow(['홍길동', 30,'개발자'])
#     content.writerow(['김철수', 25,'디자이너'])
#     content.writerow(['이영희', 28,'기획자'])
# #new라인 설정이 없어서 공백이 한줄씩 들어감. 총 9행이 생성되었음.

# with open('data.csv', 'w', newline='', encoding='utf-8') as file :
#     content = csv.writer(file)
#     content.writerow(['이름', '나이','직업'])
#     content.writerow(['홍길동', 30,'개발자'])
#     content.writerow(['김철수', 25,'디자이너'])
#     content.writerow(['이영희', 28,'기획자'])
#  #newline 설정으로 원하는 모양으로 완성. 총 5행 생성. 운영체제간의 차이로 인해 설정필요.
    
with open('data.csv', 'w', newline='', encoding='utf-8') as file :
    fieldsname = ['이름', '나이','직업']   #필드 순서를 정해줄 수 있음.
    content = csv.DictWriter(file, fieldnames=fieldsname)
    #content.writeheader()  #컬럼명도 내용에 표시해줘. 데이터가 어떤 필트에 매핑되는지 명확히 할 수 있음.
    content.writerow({'이름': '홍길동', '나이': '30', '직업': '개발자'})
    content.writerow({'이름': '김철수', '나이': '25', '직업': '디자이너'})
    content.writerow({'이름': '이영희', '나이': '28', '직업': '기획자'})
 # 딕셔너리 형태로 생성 총 4행 생성. 컬럼명은 데이터 내용에 들어가지 않음.