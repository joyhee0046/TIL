
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
