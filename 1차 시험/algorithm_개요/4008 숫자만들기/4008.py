# import itertools
# arr = ['-',['+']*2]
#
# a = tuple(itertools.permutations(arr))
# print(a)



import sys
import itertools
sys.stdin = open("sample_input.txt")

# s_time = time.time()
#
# # 연산자 개수를 가지고 연산자 리스트 만들기
# def Operator(p, m, mm, d):
#     operator=[]
#     for _ in range(p):
#         operator.append('+')
#     for _ in range(m):
#         operator.append('-')
#     for _ in range(mm):
#         operator.append('*')
#     for _ in range(d):
#         operator.append('/')
#     return operator
#
#     # idx : 현태 탐색 중인 연산자의 인덱스
#     # h_sum : 현재까지 선택한 직원들의 키의 합
# def dfs(idx, ans):
#     global max_ans, min_ans
#
#     # 이 문제는 결국 부분집합
#     # 부분집합에서 해당 원소를 선택하냐 ? 하지 않느냐 ? => 응용해보자
#     # 현재 idx가 가리키는 직원의 키를 포함하는 경우
#     for i in range(N-1):
#         if permut[idx][i] == '+':
#             ans = ans + num_li[idx]
#             idx += 1
#         if permut[idx][i] == '-':
#             ans = ans - num_li[idx]
#             idx += 1
#         if permut[idx][i] == '*':
#             ans = ans * num_li[idx]
#             idx += 1
#         if permut[idx][i] == '/':
#             ans = ans / num_li[idx]
#             idx += 1
#     dfs(0, ans)
#     min_ans = min(min_ans, ans)
#     max_ans = max(max_ans, ans)
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     # N: 숫자 수
#     N = int(input())
#     # 각 연산자의 개수 입력
#     p, m, mm, d = map(int, input().split())
#     # 연산자 리스트로 만들어서 튜플로 조합 뽑아보기
#     permut = list(set(itertools.permutations(Operator(p, m, mm, d))))
#     num_li = list(map(int, input().split()))
#
#     min_ans = 1000000
#     max_ans = -1000000
#
#     # 조합을 DFS로 구현했을 때와 비슷하게
#     # 현재 선택해야 하는 점원의 위치를 가리키는 파라미터
#     # 여태까지 선택한 조합 목록 파라미터  => 결과가 필요하다 ( 점원들의 키의 합 )
#     # 여태까지 선택된 직원들의 키의 합
#     dfs(0, 0)
#
#
#
#     # 목표 높이 B를 빼서 실제로 초과된 부분만 출력
#     print(f"#{tc} {max_ans - min_ans}")
#
# e_time = time.time()
#
# print(e_time - s_time)


###### 기범 코드
def calculate(num1, num2, operator):
    if operator == '+'
        num1 += num2
    elif operator == '-'
        num1 -= num2
    elif operator == '*'
        num1 *= num2
    elif operator == '/'
        num1 = int(num1/num2)
    return num1

def search_expression(i, result) :
