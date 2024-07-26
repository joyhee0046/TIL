# 팩토리얼 반복 
def fact(n):
    # Basis Rule: n이 1 이하인 경우 1을 반환합니다.
    if n <= 1:
        return 1
    else:
        # Inductive Rule: (n-1)로 자기 자신을 호출하는 재귀 케이스
        return n * fact(n - 1)

# 사용 예시
print(fact(5))  # 5*4*3*2*1을 계산하여 120을 출력합니다


#피보나치 반복
def fibonacci(n):
    # 기본 규칙: n이 0일 때, 0을 반환합니다.
    if n == 0:
        return 0

    # 기본 규칙: n이 1일 때, 1을 반환합니다.
    elif n == 1:
        return 1

    # 귀납 규칙: n이 2 이상일 때, F(n-1) + F(n-2)를 반환합니다.
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 사용 예시
print(fibonacci(10)) # 55를 출력합니다. (피보나치 수열: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)


#피보나치 반복에 메모이제이션 적용
def fibo1(n):
    global memo  # 전역 변수 memo를 사용할 것임을 명시
    # n이 2 이상이고 memo[n]이 아직 계산되지 않았다면 (0이면 아직 계산되지 않은 것)
    if n >= 2 and memo[n] == 0:
        # memo[n]에 fibo1(n-1)과 fibo1(n-2)의 합을 저장하여 재귀적으로 피보나치 수 계산
        memo[n] = fibo1(n-1) + fibo1(n-2)
    # 현재 n에 대한 피보나치 수를 반환
    return memo[n]

# 피보나치 수를 계산하기 위한 메모이제이션을 사용하는 배열 초기화
# 메모이제이션은 이미 계산된 결과를 저장하여 중복 계산을 피함
num = 10
memo = [0] * (num+1)  # n+1 크기의 리스트를 생성하고 모든 값을 0으로 초기화
memo[0] = 0  # 피보나치 수열의 첫 번째 수는 0
memo[1] = 1  # 피보나치 수열의 두 번째 수는 1

result = fibo1(num)  # n번째 피보나치 수를 계산
print(f"피보나치 수열의 {num}번째 수는 {result}")  # 결과 출력


#퍼뮤테이션(순열) 루프
for i in range(1, 4):  # i는 1에서 3까지의 값을 가지고, 첫 번째 자리의 숫자를 의미
    for j in range(1, 4):  # j는 1에서 3까지의 값을 가지고, 두 번째 자리의 숫자를 의미
        if j != i:  # j가 i와 같지 않은 경우에만 다음 블록을 실행
            for k in range(1, 4):  # k는 1에서 3까지의 값을 가지고, 세 번째 자리의 숫자를 의미
                if k != i and k != j:  # k가 i와 j와 같지 않은 경우에만 다음 블록을 실행
                    print(i, j, k)  # 서로 다른 세 숫자의 순열을 의미
                    
                    
#순열 반복
# selected: 선택된 값 목록
# reamin: 선택되지 않고 남은 값 목록 
def perm(selected, remain):  
    if not remain:  # 남은 요소들이 없는 경우
        print(selected)  # 선택된 요소들 출력
    else:  # 남은 요소들이 있는 경우
        for i in range(len(remain)):  # 남은 요소들의 인덱스 순회
            select_i = remain[i]  # 현재 인덱스 i에 해당하는 요소 선택
            remain_list = remain[:i] + remain[i+1:]  # 선택된 요소를 제외한 새로운 남은 요소 리스트 생성
            perm(selected + [select_i], remain_list)  # 선택된 요소를 추가한 리스트와 새로운 남은 요소 리스트로 재귀 호출

# 초기 호출로 빈 리스트와 [1, 2, 3] 리스트 사용
perm([], [1, 2, 3])


#콤비네이션 (조합) 루프
# i는 1에서 4까지의 값을 가지고, 첫 번째 자리의 숫자를 의미
for i in range(1, 5):
    # j는 i+1에서 4까지의 값을 가지고, 두 번째 자리의 숫자를 의미
    for j in range(i+1, 5):
        # k는 j+1에서 4까지의 값을 가지고, 세 번째 자리의 숫자를 의미
        for k in range(j+1, 5):
            # i, j, k가 서로 다른 세 숫자의 조합을 출력
            print(i, j, k)


#조합 반복
# arr 배열에서 n개의 요소를 선택하여 조합을 생성하는 함수
def comb(arr, n):
    result = []  # 결과를 저장할 빈 리스트 초기화

    if n == 1:  # 선택할 요소의 수가 1인 경우
        # n이 1이면 더 이상 조합할 요소가 필요 없음
        # 각 요소 자체가 하나의 조합이므로, 각 요소를 리스트로 감싸서 반환
        return [[i] for i in arr]

    # 배열의 각 요소에 대해 반복
    for i in range(len(arr)):
        elem = arr[i]  # 현재 요소를 선택
        # 현재 요소 이후의 나머지 요소들로 n-1개의 조합을 재귀적으로 생성
        for rest in comb(arr[i + 1:], n - 1):  # arr[i+1:]는 현재 요소 이후의 모든 요소를 포함
            result.append([elem] + rest)  # 현재 선택한 요소와 재귀 호출을 통해 얻은 조합을 합침

    return result  # 최종 조합 결과 반환

print(comb([1, 2, 3, 4], 3))  # [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4] 출력


# 이터레이션 라이브러리 활용
import itertools
arr = [1, 2, 3]

print(tuple(itertools.permutations(arr)))  # 순열
# ((1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1))

print(tuple(itertools.combinations(arr, 2)))  # 조합
# ((1, 2), (1, 3), (2, 3))

print(tuple(itertools.product(arr, repeat=2)))  # 중복순열
# ((1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3))

print(tuple(itertools.combinations_with_replacement(arr, 2)))  # 중복조합
# ((1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3))
