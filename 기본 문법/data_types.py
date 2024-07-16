'''
int 정수 float 실수
'''
# 지수표현. 314 ∗ 0.01
number = 314e-2

# float
print(type(number))

# 3.14
print(number)

'''
시퀀스. 여러 값을 순서대로 저장. ≠정렬
인덱스. 값이 가지는 고유번호. 특정 위치를 선택하거나 경우에 따라 수정할 수 있음.
슬라이싱. 인덱스 범위를 통해 원하는 부분의 값을 추출
길이. 값 개수 확인_len()
반복. 지정 값을 반복 처리
'''

# Hello, World!
print('Hello, World!') 
# str
print(type('Hello, World!')) 


bugs = 'roaches'
counts = 13
area = 'living room'
# f-string을 통해 Debugging roaches 13 living room 출력.
print(f'Debugging {bugs} {counts} {area}')


my_str = 'hello'
# 인덱싱
print(my_str[1]) # e
# 슬라이싱. 새로운 시퀀스를 생성.
print(my_str[2:4]) # ll
print(my_str[0:5:2]) #hlo
# 길이
print(len(my_str)) # 5

# 문자열은 불변. 덩어리에서 바꿀 수 없음. TypeError: 'str' object does not support item assignment  
my_str[1] = 'z'


# replace. 문자 변경_원본 변경하지 않고 새로운 객체를 생성하여 활용하는 방식.
text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text)  # Hello, Python!

# strip. 좌우공백 제거
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)  # 'Hello, world!'


# split. 구분자를 기준으로 분리
text = 'Hello, world!'
words = text.split(',')
print(words)  # ['Hello', ' world!']

# join. 구분자를 사용하여 병합
words = ['Hello', 'world!']
text = '-'.join(words)
print(text)  # 'Hello-world!'

'''
리스트. 변경 가능한 시퀀스
[] 표기
'''

my_list_1 = []
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
my_list = [1, 'a', 3, 'b', 5]

# 인덱싱
print(my_list[1])  # a
# 슬라이싱
print(my_list[2:4])  # [3, 'b']
print(my_list[:3])  # [1, 'a', 3]
print(my_list[3:])  # ['b', 5]
print(my_list[0:5:2])  # [1, 3, 5]
print(my_list[::-1])  # [5, 'b', 3, 'a', 1]

# 길이
print(len(my_list))  # 5

#중첩리스트 접근
my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
print(len(my_list))  # 5
print(my_list[4][-1])  # !!!
print(my_list[-1][1][0])  # w

#가변적 특징. 요소 변경
my_list = [1, 2, 3]
my_list[0] = 100

print(my_list)  # [100, 2, 3]


# append. 리스트 끝에 항목 추가
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# extend. 모든 항목을 리스트 끝에 추가
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]

# pop. 리스트 마지막 항목 반환 후 삭제_인덱스 선택 가능
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)
print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]

# reverse. 리스트 역순으로 변경 ≠정렬
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)  # [9, 1, 8, 2, 3, 1]

# sort. 리스트 (오름차순)정렬. 매개변수 활용 가능
my_list = [3, 2, 1]
my_list.sort()
print(my_list)  # [1, 2, 3]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [3, 2, 1]

'''
튜플. 변경 불가능.
() 표기 #요소가 하나일 경우 ,로 마무리 해야함 (1,)
모든 자료형 저장 가능
0개 이상 객체 포함
내부동작에 주로 사용. 안전하게 전달, 그룹화, 다중할당 등
'''

my_tuple_1 = ()
my_tuple_2 = (1,)
my_tuple_3 = (1, 'a', 3, 'b', 5)


my_tuple = (1, 'a', 3, 'b', 5)
# TypeError: 'tuple' object does not support item assignment
my_tuple[1] = 'z'


x, y = (10, 20)
print(x)  # 10
print(y)  # 20
# 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능
x, y = 10, 20


'''
레인지. 연속된 정수. 변경 불가능
증가값이 없으면 1씩 증가. 증가값이 0이면 에러
'''

my_range_1 = range(5)
my_range_2 = range(1, 10)
print(my_range_1)  # range(0, 5)
print(my_range_2)  # range(1, 10)


# 리스트로 형 변환 시 데이터 확인 가능
print(list(range(5)))   # [0, 1, 2, 3, 4]
print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 주로 반복문과 함께 활용
for i in range(1, 10):
    print(i)  # 1 2 3 4 5 6 7 8 9
for i in range(1, 10, 2):
    print(i)  # 1 3 5 7 9

'''
딕셔너리. 키-값 쌍. 순서와 중복이 없음.
key는 변경 불가능
value는 모든 자료형 사용 가능.
{}로 표시
'''

my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}
print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}

#키를 통해 값에 접근.
my_dict = {'apple': 12, 'list': [1, 2, 3]}
print(my_dict['apple'])  # 12
print(my_dict['list'])  # [1, 2, 3]
# 추가
my_dict['banana'] = 50
print(my_dict) # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}
# 변경
my_dict['apple'] = 100
print(my_dict) # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}


# get. 키에 연결된 값 반환. 없으면 None(또는 지정)
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))  # Alice
print(person.get('country'))  # None
print(person.get('country', 'Unknown'))  # Unknown

# keys. 모든 키
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # dict_keys(['name', 'age’])
for k in person.keys():
    print(k)

# values. 모든 값
person = {'name': 'Alice', 'age': 25}
print(person.values())  # dict_values ([‘Alice’, 25])
for v in person.values():
    print(v)


# items. 모든 키값쌍
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])

for k, v in person.items():
    print(k, v)


# pop 키 제거하며 연결값 반환
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}
print(person.pop('country', None))  # None
print(person.pop('country'))  # KeyError


'''
세트. 순서와 중복 없고 변경 가능.
{} 표기
'''

my_set_1 = set()    #공집합
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}
print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1}


my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}
# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}
# 차집합
print(my_set_1 - my_set_2)  # {1, 2}
# 교집합
print(my_set_1 & my_set_2)  # {3}


# add. 항목 추가. 이미 있으면 변화없음
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 'b', 3, 2, 'c', 'd', 'a’}
my_set.add(4)
print(my_set)  # {1, 'b', 3, 2, 'c', 'd', 'a’}


# remove. 항목 제거. 이미 없으면 키에러
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)  # {'b', 1, 3, 'c', 'a'}
my_set.remove(10)
print(my_set)  # KeyError

'''
기타
None : 값이 없음.
불리언 자료형 : 참과 거짓 표현
'''

variable = None
print(variable)  # None

# 함수의 return이 없는 경우 None을 반환
def func():
    print('aaa')
print(func())  # None


bool_1 = True
bool_2 = False
print(bool_1)  # True
print(bool_2)  # False
print(3 > 1)  # True
print('3' != 3)  # True


'''
데이터 복사.
'''

#변경 가능의 경우 복사한 b를 바꿔도 a가 함께 바뀜
a = [1, 2, 3, 4]
b = a
b[0] = 100
print(a)  # [100, 2, 3, 4]
print(b)  # [100, 2, 3, 4]

#변경 불가능
a = 20
b = a
b = 10
print(a)  # 20
print(b)  # 10


# 할당. 객체 참조를 복사. 동일한 위치를 보도록 됨. 분리하려면 얕은 복사.
original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list)  # [1, 2, 3] [1, 2, 3]
copy_list[0] = 'hi'
print(original_list, copy_list)  # ['hi', 2, 3] ['hi', 2, 3]


# 얕은 복사. 슬라이싱은 새로운 시퀀스 생성. 원본객체와 독립적으로 존재.
a = [1, 2, 3]
b = a[:]
print(a, b)  # [1, 2, 3] [1, 2, 3]
b[0] = 100
print(a, b)  # [1, 2, 3] [100, 2, 3]

# 얕은 복사의 한계. 중첩리스트의 경우 객체 내부주소가 같아서 함께 변경됨. 분리하려면 깊은 복사.
a = [1, 2, [1, 2]]
b = a[:]
print(a, b)  # [1, 2, [1, 2]] [1, 2, [1, 2]]
b[2][0] = 100
print(a, b)  # [1, 2, [100, 2]] [1, 2, [100, 2]]



# 깊은 복사. 모듈 사용.
import copy
original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[2][0] = 100
print(original_list)  # [1, 2, [1, 2]]
print(deep_copied_list)  # [1, 2, [100, 2]]