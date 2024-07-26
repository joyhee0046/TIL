'''
함수
def로 정의
일급객체. 변수에 할당 가능. 다른 함수에 인자로 사용 가능. 다른 함수에 의해 반환 가능.
람다표현식이라면 익명함수로 사용 가능.

매개변수 : 받을 변수. 함수 내부에서 사용.
인자 : 함수 호출에 전달되는 값.
위치 -> 기본 -> 가변 -> 가변키워드 순으로의 작성을 권장함.
'''

# Positional Arguments. 위치인자. 순서대로 할당. 필수 값
def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2


# Default Argument Values. 기본 인자값. 인자를 전달하지 않으면 기본값이 할당됨.
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
greet('Bob')  # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40)  # 안녕하세요, Charlie님! 40살이시군요.


# Keyword Arguments. 키워드 인자. 인자 이름을 명시하여 전달해야 함.
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.


# Arbitrary Argument Lists. 임의 인자 목록. 정해지지 않은 개수의 인자 처리. 매개변수 앞에 *표시로 여러 인자를 튜플처리.
def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')
calculate_sum(1, 2, 3)


# Arbitrary Keyword Argument Lists. 임의 키워드 인자 목록. 정해지지 않은 개수의 키워드 인자 처리. 매개변수 앞에 **표시로 여러 인자를 딕셔너리 처리.
def print_info(**kwargs):
    print(kwargs)
print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30}


# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)
func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')


#패킹. 다수의 값을 하나의 변수에 튜플로 담아줌. *표시로 지정 가능.
packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)

numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5


def my_func(*objects):
    print (objects) # (1, 2, 3, 4, 5)
    print(type(objects)) # <class 'tuple'>
my_func(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# <class 'tuple'>


packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5


def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(*names) # alice jane peter


#언패킹. 패킹된 값을 개별 변수에 할당.
def my_function(x, y, z):
    print(x, y, z)
my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3

names = ['aas', 'dfgd','gjgfj']
my_function(*names) #aas dfgd gjgfj