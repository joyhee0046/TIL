#bash창에서 python and.py => 실행

'''
문 : statement : 문장 _ ex) for문, while문 등
표현식 : expression : 평가 결과로 하나의 값을 도출할 수 있는 문장 _ ex) 'hello'.upper(), 'HELLO".lower() + 'everyone'.upper()  => 결과가 하나로 나옴.
평가 : evalutation : 

# 평가결과가 return.
# 식의 결과는 그냥 니가 생각하는 그 결과.
'''

# 클래스 메서드는 웬만하면 인스턴스에서 접근해서는 안되는 것과 다르게 
# 클래스 변수는 class.변수명 이 아닌, 
# 인스턴스.변수명 으로 접근해도 괜찮은 건가요?
class Person:
    population = 0    # 클래스 변수

    def __init__(self, name):    #생성자 메소드
        self.name = name
        Person.num_of_population()

    def info(self):   #인스턴스 메소드
        print(f'제 이름은 {self.name} 입니다.')
        return self.name

    @classmethod    #클래스 메소드
    def num_of_population(cls):
        cls.population += 1
        Person.population += 1



    def __str__(self):  #매직메소드_사용자를 위한 출력정리
        return f'이 객체의 이름은 {self.name}'
    
    def __repr__(self):   #매직메소드_개발자를 위한 객체정보_속성 타입 메소드 등
        return "Person()"

    # @staticmethod
    # def name_change(instance):
    #     instance.name = '개똥이'
    @staticmethod  #정적메소드
    def esihed(sgrse) :


viktor = Person('viktor')  #인스턴스
viktor.population = 10
harry = Person('harry')
# 인스턴스가 클래스 메서드를 호출하게 되면?
viktor.num_of_population()
print(Person.population)
# 인스턴스가 클래스 변수를 조회하는 코드는?
print(viktor.population)
print(harry.population)



# 클래스 메서드에서 cls.변수명 으로 
# 클래스 변수에 접근하는 이유가 무엇인가요? 
# cls를 사용하지 않아도 class Person이라면 
# Person.변수명 으로 접근할 수 있지 않나요? 
# 유지보수나 가독성을 위해서인가요?

# 정의된 위치 상관 없이(ex. 클래스 내부) 인스턴스 변수에 접근하고 
# 수정할 수 있는 함수면 모두 인스턴스 메서드인걸까요?

# viktor.name_change(viktor)
# print(viktor.name)

# 함수에서 print와 return을 동시에 사용하는 경우는?
info = viktor.info()
print(info)

print(viktor)

a = repr(viktor)
print(a)
# MRO의 탐색 순서는?