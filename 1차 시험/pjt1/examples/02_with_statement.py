# with문 : 리소스를 자동 해제. 파일이 종료됨.
'''
with 표현식 as 변수:
    내부 실행 코드
'''

content = open('users.csv')
# print(content)
print(content.read())

with open('example.txt', 'r') as file_txt :
    print(file_txt.read())

with open('users.csv', 'r') as file_csv :
    print(file_csv.read()) 

print(content.read())   #위에서 다 읽었기 때문에_순회종료.메모리에 남아있음_ 읽을 내용이 없어서 출력값이 없는 것.
print(file_csv.read())   #ValueError: I/O operation on closed file. 파일이 닫혔다.