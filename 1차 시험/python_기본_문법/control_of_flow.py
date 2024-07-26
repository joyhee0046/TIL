'''
제어문. 코드의 실행 흐름 제어. 조건에 따라 블록을 실행하거나 반복적으로 실행
조건문. 반복문. 반복제어
'''

dust = 35
if dust > 150 :
    print('매우 나쁨')
elif dust > 80 :
    print('나쁨')
elif dust >30 :
    print('좋음')
else : 
    print('매우 좋음')
    

#for 반복 횟수가 정해진 경우. 리스트 튜플 문자열 등에서
items = ['apple', 'banana', 'coconut']
for item in items:
    print(item)

numbers = [4, 6, 10, -8, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)  # [8, 12, 20, -16, 10]

elements = [['A', 'B'], ['c', 'd']]
for elem in elements:
    for item in elem:
        print(item)


#while 반복 횟수가 불명확하거나 조건에 따라 종료해야 할 경우.
a = 0
while a < 3:
    print(a)
    a += 1
print('끝')


# break
for i in range(10):
    if i == 5:
        break
    print(i)  # 0 1 2 3 4

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1 3 5 7 9

# pass
for i in range(10):
    pass  # 아무 작업도 안함


#List Comprehension. 간결하고 효율적인 리스트 생성 방법
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)  # [1, 4, 9, 16, 25]

data1 = [[0] * (10) for _ in range(10)]
# 또는
data2 = [[0 for _ in range(10)] for _ in range(10)]


#내장함수 enumerate 를 사용한 반복_인덱스와 원소를 동시에 접근하여 튜플로 만들어줌.
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')
