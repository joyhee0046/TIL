# # 아래에 코드를 작성하시오.
# class User :
#     user_count = 0
#     def __init__(self, name, email) :
#         self.name = name
#         self.email = email
#         User.user_count+=1

#     @staticmethod
#     def description() :
#         print("SNS 사용자는 소셜 네트워크 서비스를 이용하는 사람을 의미합니다.")
    
# us1 = User("Alice", "alice@example.com")
# us2 = User("Bob", "bob@example.com")
# print(us1.name)
# print(us1.email)
# print(us2.name)
# print(us2.email)
# print(f"현재까지 생성된 사용자 수: {User.user_count}")
# User.description()


class User:
    user_count = 0

    # 특수한 매직 메서드는
    # 객체 구현시, 해당 프로그래밍 과정에서 반드시 필요한 기능이 있다면
    # 그때 매직메서드 조사 한 수에 작성해도 문제가 되지 않는다.

    # 매직 메서드 -> 특정 상황에 호출된다.
    # 그 외에는 일반적인 함수랑 다를바가 단 1도 없다.
    # 일반 함수와 완전히 동일하게 동작하기 떄문에, 기본인자를 추가할 수도 있다.
    def __init__(self, name, email, age=30):
        self.name = name
        self.email = email
        self.age = age
        User.user_count += 1

    # 실습 2-5처럼 다중 상속으로 인한, class간의 관계가 복잡해진 경우가 아니라면,
    # 그리고, 그렇게 복잡해 진 상황 속에서도, 특정 BaseClass가 공통된 staticmethod를
    # 정의할게 아니라면...
    # staticmethod는 항상... 인스턴스 변수나, 클래스 변수 등에 접근하지 않을 내용들만 다룬다.,
    # 그게 아니라면, 인스턴스 메서드, 클래스 메서드로 명시적으로 메서드를 정의하는게 좋다.
    @staticmethod
    def description():
        print('SNS 사용자는 소셜 네트워크 서비스를 이용하는 사람을 의미합니다.')

    # 소멸자
    def __del__(self):
        print('악')

# 인스턴스 생성
user1 = User('Alice', 'alice@example.com')
# del 키워드로 강제로 소멸 시킬수도 있다.
# del user1
user2 = User('Bob', 'bob@example.com')

# 각 인스턴스의 name과 email 출력
user1.name = '다른 어떤 값'
print(user1.name)
print(user1.email)
print(user2.name)
print(user2.email)
print(user1.age)

# User 클래스의 user_count 출력
print(f'현재까지 생성된 사용자 수: {User.user_count}')

# description 스태틱 메서드 호출
User.description()

# dir 내장함수 사용해서, 해당 type이 가지고 있는 메서드, 속성, 등등을 확인할 수 있다.
print(dir(user1))
# 매직메서드는 파이썬 코드가 실행될 때, 내부 설계적으로 실행에 필요한 로직들이 담겨있어서
# 별도로 정의하지 않더라도, class 정의시 기본 class 상속받아와서
# 기본적인 매직메서드는 모두 정의되어 있는 상태이다.