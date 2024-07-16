'''
클래스. 타입을 표현하는 방법.
객체 생성을 위한 설계도
데이터와 기능을 묶는 방법 정의
객체 : 메모리에 할당된 속성과 행동 등 모든 것.
클래스로 만든 객체 : 인스턴스_아이유는 가수 클래스의 인스턴스 이다.
클래스를 만든다 = 타입을 만든다
하나의 객체는 특정 타입의 인스턴스이다.

객체. 타입_어떤 연산자(오퍼레이터)와 조작(메소드)이 가능한지.
        속성_어떤 상태(데이터)를 가지는지.
        조작_어떤 행위(함수)를 할 수 있는지.
'''
# 클래스 정의
class Person:
    blood_color = 'red'
    def __init__(self, name):
        self.name = name
    def singing(self):
        return f'{self.name}가 노래합니다.'

# 인스턴스 생성
singer1 = Person('iu')
# 메서드 호출
print(singer1.singing())  
# 속성(변수) 접근
print(singer1.blood_color)

'''
클래스의 구성요소.
생성자 함수. 객체 생성시에 자동 호출. __init__하면 객체 초기화
클래스 변수. 내부선언변수. 클래스로 생성된 모든 인스턴스들이 공유.
class.class_variable로 클래스 변수 참조. 

메서드 종류
인스턴스 메서드/클래스 메서드/정적 메서드
인스턴스 메서드 : 클래스에서 생성된 인스턴스에서 호출할 수있는 메서드. 조작동작. 첫번째 변수로 자신을 전달받음_self
        생성자 메서드 = 인스턴스 메서드. 객체 생성시에 자동 호출. 
클래스 메서드 : 클래스가 호출하는 메서드. 조작 동작. @classmethod를 데코레이터로 사용하여 정의. 첫번째 변수로 호출_cls
정적 메서트 : 클래스와 인스턴스의 특징의 상호작용없이 독립적으로 동작. @staticmethod를 데코레이터로 사용하여 정의. 필수 매개변수 없음.

인스턴스와 클래스의 이름공간
클래스를 정의하면 클래스와 해당하는 이름공간이 생성됨.
인스턴스를 정의하면 객체가 생성되고 독립적 이름공간 생성
인스턴스에서 속성에 접근하면 인스턴스-> 클래스로 탐색.
class를 정의하면 메모리(이름공간)에 생성자 함수와 클래스 변수가 저장됨.
인스턴스를 생성하면 인스턴스별로 따로 저장된다.

누가 어떤 메서드를 사용할지
클래스 : 클래스 메서트, 스태틱(정적) 메서드
인스턴스 : 인스턴스 메서드
'''
# 인스턴스 메서드
class Person:
    def __init__(self, name):
        self.name = name
        print('인스턴스가 생성되었습니다.')
    def greeting(self):
        print(f'안녕하세요. {self.name}입니다.')
person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.


# 클래스 메서드
class Person:  #클래스 이름공간1
    count = 0   #클래스 이름공간1
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')

person1 = Person('iu')     #인스턴스별 이름공간1
person2 = Person('BTS')    #인스턴스별 이름공간2



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


'''
상속. 계층구조에 활용. 클래스를 정의할 때  상속할 클래스를 적어주면 됨._class 새클래스(상속클래스) :
    상속 없이는 별도로 구현하기 어려움. 클래스를 구분하여 정의해도 메서드를 중복시킬 수 있음.
다중상속. 둘 이상의 상위클래스로부터 여러 행동이나 특징을 상속받을 수 있음. 상속받은 모든 클래스의 요소 활용 가능. 중복된 속성이나 메서드가 있으면 상속순서로 결정.
    상속 순서 : 본인이 한 재정의가 우선. class 새클래스(상속1,상속2) :_에서는 상속1이 우선.
    다이아몬드 문제 : MRO알고리즘_깊이우선 왼-오 탐색이므로 새클래스>상속1>상속2(>상속1과2가 상속받은 클래스) 순서
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')
class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)
# 부모 Person 클래스의 talk 메서드를 활용
p1.talk()  # 반갑습니다. 박교수입니다.
# 부모 Person 클래스의 talk 메서드를 활용
s1.talk()  # 반갑습니다. 김학생입니다.


# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return f'안녕, {self.name}'
class Mom(Person):
    gene = 'XX'
    def swim(self):
        return '엄마가 수영'
class Dad(Person):
    gene = 'XY'
    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    def cry(self):
        return '첫째가 응애'
baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY

'''
super() : 부모 클래스(다음 클래스)의 객체를 반환하는 내장함수. 
    단일상속에서는 이름을 지정하지 않고 부모클래스 참조 가능.
    다중상속에서는 MRO를 따름. 
MRO : 이미 한번 찾은 값에 대해 부모 클래스들이 여러 번 액세스 되지 않도록함.
    클래스의 흐름은 보존하며, 각 클래스를 한번만 호출하고, 우선순위에 영향을 주지 않으며 서브 클래스를 만드는 단조적 구조 형성
    프로그래밍 언어의 신뢰성있고 확장성있는 클래스 설계 가능.
    메서드 호출 순서가 예측가능해지며 코드의 재사용성과 유지보수성 향상.
'''
# 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # Person의 init 메서드 호출
        super().__init__(name, age, number, email)
        self.student_id = student_id


# 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')
class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')


'''
매직 메서드(스페셜 메서드/인스턴스 메서드)
특정 상황에서 자동 호출
__str__(self) 등 더블언더스코어를 사용함
    __str__(self)는 print로 호출된 객체 출력을 문자열로 표현 변경. 상태말고 내용을 볼 수 있도록.

데코레이터(Decorator)
다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수.
'''

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

'''
이터레이터(Iterator) : 반복가능한 객체의 요소를 하나씩 반환하는 객체
    내부적으로 for 문이 동작할 때 반복가능한 객체에 대해 iter() 호출.
    iter()에서는 메서드 __next()__를 정의하는 이터레이터 객체를 돌려줌.
    __next()__에서는 반복가는 객체를 한번에 하나씩 접근하도록 제어하고 남은게 없으면 StopIteration으로 for문을 종료
'''
class Reverse :   #이터레이터 동작을 클래스로 정의
    def __init__(self, data): 
        self.data = data  #값이 들어오면 내용 저장
        self.index = len(data)   #값이 들어오면 길이 확인
    def __iter__(self) :
        return self
    def __next__(self) :
        if self.index == 0 : 
            raise StopIteration  #강제종료 발생
        self.index = self.index -1 
        return self.data[self.index]
    
rev = Reverse('abc')
for char in rev :
    print(char)

'''
제너레이터(Generator). 이터레이터를 간단하게 만드는 함수.
    메모리 효율성(한번에 하나만 생성_전체시퀀스를 한번에 로드하지 않음. 대용량 파일 처리 가능_각줄 처리)
    무한 시퀀스 처리(무한 루프로 무한 시퀀스 생성 가능. 끝없는 데이터 스트림 처리에 유용)
    지연 평가(필요할때만 값 생성_불필요한 계산을 피해서 성능 최적화. 연산지연_복잡한 연산을 지연수행하여 필요한 시점에만 동작)
    일반 함수처럼 작성하되 yield문으로 값을 반환.
    클래스기반의 iter만들지않아도 자동 생성.
        self.data나 self.index같은 인스턴스 변수를 통한 접근보다 더 쉽고 명료함.
    반복가능 객체를 생성 호출하면 다음 순서를 기억함. 호출 전까지는 값을 메모리에 올리지 않음_지연평가. 제너레이터를 사용하지 않으면 선언과 동시에 메모리 사용.
return : 값을 반환하고 함수 종료. 호출시마다 전체 실행. 호출 상태가 유지되지 않음.
yield : 값을 반환하고 대기. 현재 상태를 유지. 호출 시 중단시점부터 다시 실행. 

데이터 분석 시 큰 데이터를 한번에 받아서(메모리에 올려서) 처리할 수 없는 경우
데이터를 개발자가 원하는 만큼 가져와서 처리하고 다시 받아오는 행위를 반복하며 분석 진행._메모리 효율성
'''
def generate_numbers():
    for i in range(3):
        yield i

for number in generate_numbers():
    print(number)  # 0 1 2


def reverse_generator(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse_generator('abc'):
    print(char) # c b a


# 무한 시퀀스
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
gen = infinite_sequence()  #대기상태 값 확인 불가.
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

def fibonacci_generator():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2
gen = fibonacci_generator()
# 첫 10개의 피보나치 수를 출력
for _ in range(10):
    print(next(gen))  # gen.__next__()와 동일
#1~다시 하는거 아님. 이전 동작을 기억. 과거로 돌아갈수는 없음_필요하다면 저장해두어야.
print(next(gen))  # 11번째 피보나치 수  
print(next(gen))  # 12번째 피보나치 수


# 대용량 데이터 처리 
def read_large_file_with_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:  #전체파일을 로드하지 않음.
            yield line.strip()
# 예제 파일 경로
file_path = 'large_data_file.txt'  
# 제너레이터 사용하여 파일 읽기 및 처리
for line in read_large_file_with_generator(file_path):
    print(line)

'''
제너레이터 표현식
리스트 컴프리헨션과 비슷하지만 대괄호 대신 소괄호를 사용.
리스트보다 메모리 덜 씀
간결하지만 가독성 떨어짐.

제너레이터 요소를 모두 참조한 경우 재사용 불가능. 다시 불러서 재할당 필요.
'''
def gen_nums() :
    for i in range(int(1e6)) :
        yield i
nums = gen_nums()

nums = (i for i in range(int(1e6)))  #제너레이터 표현식

def generate_func():
    print('1번')
    yield 1
    print('2번')
    yield 2

gen = generate_func()
print(next(gen)) # 1번 1
print(next(gen)) # 2번 2
print(next(gen)) # StopIteration

for i in gen:
    print(i)
#원래는 1번1 2번2가 나와야 하지만, 앞에서 사용했기 때문에 아무것도 출력되지 않음.

gen = generate_func()  #재할당하여 사용
for i in gen:
    print(i)


'''
에러와 예외
문법 에러 : Syntax Error : 문법오류나 잘못된 할당. 소괄호문제 등 코딩 문제
예외 : Exception : 내장 예외_파이썬에서 이미 정의된 상황에 대한 처리.
    ZeroDivisonError : 나누기 또는 모듈 연산의 두번째 인자가 0일 때.
    NameError : 지역 또는 전역 이름을 찾을 수 없을 때
    TypeError : 타입 불일치 또는 인자 누락, 인자 초과, 인자 타입 불일치
    ValueError : 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받음
    IndexError : 시퀀스 인덱스가 범위를 벗어날 때 발생
    KeyError : 딕셔너리에 해당 키가 존재하지 않는 경우
    ModuleNotFoundError : 모듈을 찾을 수 없을 때 발생
    ImportError : import 이름을 찾을 수 없을 때 발생
    KeyboardInterrupt : 사용자가 ctrl-C또는 del을 누를 때 발생. 무한루프 강제종료
    IndentationError : 잘못된 들여쓰기 등 문법 오류
예외처리 : Exception Handling : 예외 발생 시에 적절하게 처리되도록 하는 방법. 복수처리 가능_하위 예외클래스부터 확인하도록 
    try : 예외 발생 가능 코드
    except : 예외 발생 시 실행 코드
    else : 예외 발생하지 않을 시 실행 코드
    finally : 예외발생여부에 무관하게 항상 실행할 코드
'''
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
# 0으로 나눌 수 없습니다.


try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')
"""
숫자입력 : a
숫자가 아닙니다.
"""


try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')


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
