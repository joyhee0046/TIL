content = open('users.csv')
# print(content)
print(content.read())

with open('example.txt', 'r') as file:
    print(file.read())

with open('users.csv', 'r') as file:
    print(file.read())
# with 블록이 종료되면 파일이 자동으로 닫힘. -> 리소스를 해제한다.

print(content.read())
print(file.read())