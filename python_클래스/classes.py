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
