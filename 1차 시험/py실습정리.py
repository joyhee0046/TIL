password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
fst = password[28:35] # 28번째부터 35번째까지에 작성된 글자
snd = password[113:118] # 113번부터 5글자
trd = password[68:65:-1] # 66번부터 68번까지 뒤집어서
frth = password[325:321:-1] # 322번부터 4글자씩 뒤집어서
fith = password[365:371] # 365번부터 작성되어있는 python
print(f'{fst} {snd} {trd} {frth} "{fith}".') # life is short you need "python".

# 학생들의 이름과 점수를 딕셔너리에 저장
students = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 88, "Eve": 95}
# students 변수에 할당된 데이터 타입이 어떤 타입인지 출력
print(type(students))
# 모든 학생의 평균 점수 = 모든 value의 합 / 전체 학생 수
avg_score = sum(students.values()) / len(students)
# 평균점수를 소수점 5자리까지 표현. 6자리에서 반올림
print(f'모든 학생들의 평균 점수 {avg_score:.5f}')
# 80점이상인 학생만 리스트컴프레션을 이용하여 리스트 생성
top_students = [key for key, value in students.items() if value >= 80]
# sorted(정렬할 데이터, key 파라미터, reverse 파라미터) key는 아이템의 두번째 값(인덱스1번)으로 하겠다.
print(sorted(students.items(), key=lambda item: item[1], reverse=True))
# students에서 점수는 value()에 위치. 최대와 최소를 확인하고 차이 계산
print(f'점수 차 : {max(students.values()) - min(students.values())}')
# 각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력_k,v를 items로 다 받거나 k를 받아서 v를 호출하는 방법도 가능
# for key, value in students.items():
#     if value > avg_score:
#         status = '이상'
#     else:
#         status = '이하'
#     print(f'{key}인 학생의 점수 {students[key]}값은 평균 {status}이다.')
for key in students:
    if students[key] > avg_score:
        status = '이상'
    else:
        status = '이하'
    print(f'{key}인 학생의 점수 {students[key]}값은 평균 {status}이다.')

username = 'user123'  # 할당

#아래를 모듈로 저장하기 위해서는 그냥 새 py파일에 저장하면 됨
def filter_adults(users):  #성인필터
    # uage, uage에 할당된, users에서 뽑아서, uage의 age가 18이상인
    return [user for user in users if user['age'] >= 18]
def filter_active_users(users):  #활성화필터
    # uact, uact에 할당된, users에서 뽑아서, uact의 is_active가 True인
    return [uact for uact in users if uact['is_active']]
def filter_adult_active_users(users):  #종합필터
    # user, user에 할당된, users에서 뽑아서, user의 age가 18이상이고 user의 is_active가 True인
    return [user for user in users if user['age'] >= 18 and user['is_active']]

# movies와 ratings 리스트를 순회하며 짝지어서 딕셔너리로 만들어서 새 리스트에 담기
new_movies_list = []
for title, rating in zip(movies, ratings):
    temp_dict = {'title': title, 'rating': rating}
    new_movies_list.append(temp_dict)
print(new_movies_list)
# 같은 결과를 리스트컴프레인션으로 작성
# com_movies = [{'title': title, 'rating': rating} for title, rating in zip(movies, ratings)]

####################################

class Product:  #클래스 정의
    product_count = 0  # 인스턴수 수를 기록한 클래스 변수
    def __init__(self, name, price):  # 생성자 메서드
        self.name = name  # 값 할당
        self.price = price
        Product.product_count += 1  # 인스턴스 생성마다 1씩 증가
    def display_info(self):  # 인스턴스 메서드 정의
        # display_info 메서드의 주어진 역할 : 생성된 인스턴스의 정보 출력
        print(f"상품명: {self.name}, 가격: {self.price}원")
        # 윗줄 지우고  # return f"상품명: {self.name}, 가격: {self.price}원" ⇒ print(product1.display_info())로 사용 가능
        return self.name, self.price  # product2.display_info()만으로도 출력 가능

#상속관계 확인
class Animal:  #클래스 정의
    def __init__(self, name):  #생성자 메서드, 인스턴스는 name을 변수로 가지게 된다.
        self.name = name
    def speak(self):  #speak메서드_자식 클래스에 오버라이딩
        pass
class Dog(Animal): #클래스 정의, Animal을 상속받음
    def speak(self):  #메서드 오버라이딩, Woof!을 반환
        return "Woof!"
class Flyer:  #클래스 정의
    def fly(self):
        return "Flying"
class Swimmer:
    def swim(self):
        return "Swimming"
class Duck(Animal, Flyer, Swimmer):  #클래스 정의, 다중상속,Duck.fly나 Duck.swim도 동작.
    def __init__(self, name):
        super().__init__(name)
    def speak(self): #메서드 오버라이딩
        return "Quack!"
def make_animal_speak(animal):  #함수 정의
    print(animal.speak()) #각 객체의 speak메서드를 호출하고 출력하도록.

class MovieTheater: #클래스 정의
    def __init__(self, name, total_seats):  #생성자메서드로 인스턴스변수 정의
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0  #인스턴스변수. 0을 할당받는다.
    def __str__(self) -> str: #인자 값을 확인할 수 있도록 변수 매직메서드 사용
        return self.name  #인스턴스를 print하면 인스턴스의 name이 출력 되도록 하려면 return사용
    def reserve_seat(self):  #인스턴스메서드 정의
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            return "좌석 예약이 완료되었습니다."
        else:
            return "예약 가능한 좌석이 없습니다."
class VIPMovieTheater(MovieTheater):   #기존 클래스를 상속받는 새 클래스 정의
    def __init__(self, name, total_seats, vip_seats):
        super().__init__(name, total_seats)
        self.vip_seats = vip_seats  #인스턴스 변수
    def reserve_vip_seat(self):  #메서드 생성
        if self.vip_seats > 0:
            self.vip_seats -= 1
            return "VIP 좌석 예약이 완료되었습니다."
        else:
            return "예약 가능한 VIP 좌석이 없습니다."
    def reserve_seat(self):  #메서드 오버라이딩.
        if self.vip_seats > 0:
            return self.reserve_vip_seat()  #인스턴스 메서드 호출
        else:
            return super().reserve_seat()  #상속받은 부모 클래스 메서드 호출
class Theater(MovieTheater): #기존 클래스를 상속받는 자식클래스 정의
    total_movies = 0
    @classmethod #클래스 메서드
    def add_movie(cls):
        cls.total_movies += 1
        return "영화가 성공적으로 추가되었습니다."
    @staticmethod  #정적메서드_무조건 밖에서 가져올거임_남의 메소드 사용가능
    def description(mt):
        print(f"영화관 이름: {mt.name}")
        print(f"총 좌석 수: {mt.total_seats}")
        print(f"예약된 좌석 수: {mt.reserved_seats}")
        print(f"총 영화 수: {Theater.total_movies}")
    @staticmethod  #정적메서드
    def classinfo():
        print("이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.")
        print("영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.")

# dir 내장함수 사용해서, 해당 type이 가지고 있는 메서드, 속성, 등등을 확인할 수 있다.
print(dir(인스턴스))

