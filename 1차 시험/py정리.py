# 314 ∗ 0.01
number = 314e-2

my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
print(my_list[-1][1][0])  # w

# dict get
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))  # Alice
print(person.get('country'))  # None
print(person.get('country', 'Unknown'))  # Unknown

# dict
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # dict_keys(['name', 'age’])
print(person.values())  # dict_values ([‘Alice’, 25])
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])

print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}

print(person.pop('country', None))  # None
print(person.pop('country'))  # KeyError


# 명시적 형변환
# ValueError: invalid literal for int() with base 10: '3.5'
print(int('3.5'))

#단축평가__결과는 걍 외워버려ㅋ
vowels = 'aeiou'
#and는 뒤를 먼저보고 ,or는 앞을 먼저보는건데, 0은 언제나 반대의 경우까지 고려하게 됨.
print(('a' and 'b') in vowels)  # False
print(('b' and 'a') in vowels)  # True
print(('a' or 'b') in vowels)  # True
print(('b' or 'a') in vowels)  # False
print(3 and 5)  # 5
print(3 and 0)  # 0
print(0 and 3)  # 0
print(0 and 0)  # 0
print(5 or 3)  # 5
print(3 or 0)  # 3
print(0 or 3)  # 3
print(0 or 0)  # 0

# break   반복빠져나오기
for i in range(10):
    if i == 5:
        break
    print(i)  # 0 1 2 3 4
# continue   다음반복진행하기
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1 3 5 7 9
# pass   동작하지않고 진행하기
for i in range(10):
    pass  # 아무 작업도 안함

# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)  #1
    print('pos2:', pos2)  #2
    print('default_arg:', default_arg)  #3
    print('args:', args)  #(4,5,6)
    print('kwargs:', kwargs)   #{'key1': 'value1', 'key2': 'value2'}
func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')

# 스코프
a = 1
b = 2
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a, b, c)  # 10 2 500
    local(500)
    print(a, b, c)  # 10 2 3
enclosed()
print(a, b)  # 1 2


#################################

# 클래스 정의
class Person:
    count = 0
    blood_color = 'red'
    def __init__(self, name):
        self.name = name
    def singing(self):
        return f'{self.name}가 노래합니다.'
    @classmethod   #클래스 메서드
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')
# 인스턴스 생성
singer1 = Person('iu')
# 메서드 호출
print(singer1.singing())
# 속성(변수) 접근
print(singer1.blood_color)


# 정적 메서드
class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]
    @staticmethod
    def capitalize_string(string):
        return string.capitalize()
text = 'hello, world'
reversed_text = StringUtils.reverse_string(text)
print(reversed_text)  # dlrow ,olleh
capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text)  # Hello, world


# 데코레이션
def my_decorator(func):
    def wrapper():
        # 함수 실행 전에 수행할 작업
        print('함수 실행 전')
        # 원본 함수 호출
        result = func()
        # 함수 실행 후에 수행할 작업
        print('함수 실행 후')
        return result
    return wrapper
@my_decorator
def my_function():
    print('원본 함수 실행')
my_function()
"""
함수 실행 전
원본 함수 실행
함수 실행 후
"""


try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')

## 정규표현식
import re
# 정규표현식을 사용한 간단한 패턴 매칭 예제
pattern = r'\d+'  # 숫자(\d)가 하나 이상(+)인 패턴
text = 'There are 24 apples and 42 oranges.'
matches = re.findall(pattern, text)
print(matches)  # ['24', '42']


import re
pattern_raw = r'\d+'  # raw string으로 작성
pattern_normal = '\\d+'  # 일반 문자열로 작성
text = 'There are 24 apples and 42 oranges.'
matches_raw = re.findall(pattern_raw, text)
matches_normal = re.findall(pattern_normal, text)
print(matches_raw)  # ['24', '42']
print(matches_normal)  # ['24', '42']


import re
text = 'Example 123, demo_789.'
# 임의의 한 문자
print(re.findall(r'.', text))  #['E', 'x', 'a', 'm', 'p', 'l', 'e', ' ', '1', '2', ....
# 숫자
print(re.findall(r'\d', text))  #['1', '2', '3', '7', '8', '9']
# 숫자가 아닌 문자
print(re.findall(r'\D', text))  #['E', 'x', 'a', 'm', 'p', 'l', 'e', ' ', ',', ' ', 'd', 'e', ...
# 단어 문자
print(re.findall(r'\w', text))  #['E', 'x', 'a', 'm', 'p', 'l', 'e', '1', '2', '3', 'd', ...
# 단어 문자가 아닌 문자
print(re.findall(r'\W', text))  #[' ', ',', ' ', '.']
# 공백 문자
print(re.findall(r'\s', text))  #[' ', ' ']
# 공백 문자가 아닌 문자
print(re.findall(r'\S', text))  #['E', 'x', 'a', 'm', 'p', 'l', 'e', '1', '2', '3', ',', 'd', 'e'...


import re
text = 'Start and end. Start and stop.'
# 문자열의 시작
print(re.findall(r'^Start', text))   #['Start']
# 문자열의 끝
print(re.findall(r'stop$', text))  #[]
# 문자열의 끝
print(re.findall(r'stop\.$', text))  #['stop.']


import re
text = 'a B 1 c D 2 e F 333'
# 대문자 알파벳 매칭
print(re.findall(r'[A-Z]', text))  #['B', 'D', 'F']
# 숫자 매칭
print(re.findall(r'[0-9]', text))  #['1', '2', '3', '3', '3']
# 소문자, 대문자, 숫자 매칭
print(re.findall(r'[a-zA-Z0-9]', text))  #['a', 'B', '1', 'c', 'D', '2', 'e', 'F', '3', '3', '3']
# 소문자 제외 매칭
print(re.findall(r'[^a-z]', text))  #[' ', 'B', ' ', '1', ' ', ' ', 'D', ' ', '2', ' ', ' ', 'F', ' ',...
 이상 매칭
print(re.findall(r'[0-9]+', text))  #['1', '2', '333']


import re
text = 'My phone number is 123-456-7890.'
# 그룹화
pattern = r'(\d{3})-(\d{3})-(\d{4})'
match = re.search(pattern, text)
if match:
    print(match.group(0))  # 매칭된 전체 문자열  123-456-7890
    print(match.group(1))  # 첫 번째 그룹에 매칭된 문자열  123
    print(match.group(2))  # 두 번째 그룹에 매칭된 문자열  456
    print(match.group(3))  # 세 번째 그룹에 매칭된 문자열  7890
    print(match.groups())  # 모든 그룹에 매칭된 문자열을 튜플로 반환  ('123', '456', '7890')


# 이름 있는 그룹
pattern = r'(?P<area_code>\d{3})-(?P<exchange>\d{3})-(?P<number>\d{4})'
match = re.search(pattern, text)
if match:
    print(match.group('area_code'))  #123
    print(match.group('exchange'))  #456
    print(match.group('number'))  #7890


import re
text = 'Please call 123-456-7890 for assistance.'
pattern = r'\d{3}-\d{3}-\d{4}'
replacement = '[phone number]'
new_text = re.sub(pattern, replacement, text)
print(new_text)  # Please call [phone number] for assistance.


import re
def mask_phone_number(match):
    return f'[{match.group()}]'
text = 'Contact us at 123-456-7890 or 987-654-3210.'
pattern = r'\d{3}-\d{3}-\d{4}'
new_text_with_function = re.sub(pattern, mask_phone_number, text)
print(new_text_with_function)  #Contact us at [123-456-7890] or [987-654-3210].


import re

# 이메일 주소 검증
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  # 문자@문자.문자 의 형식인지
emails = ['test@example.com', 'invalid-email', 'user.name@domain.co']  # valid invalid valid
for email in emails:
    if re.search(email_pattern, email):
        print(f'{email} is valid')
    else:
        print(f'{email} is invalid')

# Gmail 주소 검증
gmail_pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'  #문자@gmail.com 의 형식인지
emails = [
    'test@gmail.com',  #is a valid
    'user.name@gmail.com',  #is a valid
    'invalid-email',  #is not a valid
    'user@domain.com',  #is not a valid
]
for email in emails:
    if re.search(gmail_pattern, email):
        print(f'{email} is a valid Gmail address')
    else:
        print(f'{email} is not a valid Gmail address')


# 전화번호 검증
phone_pattern = r'^\d{3}-\d{3}-\d{4}$'  #숫자3-숫자3-숫자4 의 형식인지
phones = ['123-456-7890', '123-45-6789', '123-4567-890'] # valid invalid invalid
for phone in phones:
    if re.search(phone_pattern, phone):
        print(f'{phone} is valid')
    else:
        print(f'{phone} is invalid')

# 010으로 시작하는 전화번호 검증
phone_pattern = r'^010-\d{3,4}-\d{4}$'  #010-숫자3이나4-숫자4 의 형식인지
phones = ['010-1234-5678', '010-234-5678', '011-345-6789', '010-4567-8901']  #is a valid / is a valid/ is not a valid/ is a valid
for phone in phones:
    if re.search(phone_pattern, phone):
        print(f'{phone} is a valid number')
    else:
        print(f'{phone} is not a valid number')

# URL 검증
url_pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
urls = ['http://example.com', 'https://www.example.com/234', 'invalid-url']  # valid valid invalid
for url in urls:
    if re.search(url_pattern, url):
        print(f'{url} is valid')
    else:
        print(f'{url} is invalid')


