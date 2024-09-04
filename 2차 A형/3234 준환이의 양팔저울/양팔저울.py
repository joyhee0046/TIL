import sys
sys.stdin = open('sample_input (1).txt', 'r')

from math import factorial

def dfs(pick, l_sum, r_sum):  # 이번에 선택한 추, 왼무게, 오른무게
    global result

    # 오른쪽 무게의 총합이 왼쪽에 올라가 있는 무게의 총합보다 커지면 중단
    if l_sum < r_sum:
        return

    # 왼 무게가 전체무게 절반을 넘으면 나머지 추에 대한 모든 조합 실행가능. 탐색없이 결과에 더해주기.
    if l_sum >= total_w:
        # (2^남은추갯수 * 남은추갯수!)만큼 결과에 더해주기
        result += (2 ** (N - pick)) * factorial(N - pick)
        return

    for i in range(N):
        # 이미 사용한 추면 넘어가기
        if visited[i]:
            continue
        # 사용했다고 체크해주기
        visited[i] = True
        # 선택한 추를 왼쪽에 놓는 경우
        dfs(pick + 1, l_sum + arr[i], r_sum)
        # 선택한 추를 오른쪽에 놓는 경우
        dfs(pick + 1, l_sum, r_sum + arr[i])
        # 원복
        visited[i] = False

# 주어진 입력 받기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 결과_가능한 경우의 수
    result = 0
    # 무게 추 사용여부 체크할 배열
    visited = [False] * N
    # 전체 무게 합의 절반_왼저울 무게와 비교할 정보
    total_w = sum(arr) / 2

    # n번째 추를 시작추로 하는 DFS 시작_시작추는 무조건 왼
    for n in range(N):
        visited[n] = True
        dfs(1, arr[n], 0)
        # 탐색이 끝나면 원복. 다음 탐색 해야하니까.
        visited[n] = False
    # 정답 출력
    print(f"#{tc} {result}")