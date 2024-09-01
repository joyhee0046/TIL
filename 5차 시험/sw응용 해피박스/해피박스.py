import sys
sys.stdin = open('sample_input(1).txt', 'r')

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(M)]

    # 2차원 배열 만들기
    dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

    # 1부터 시작하는 이유 :
    # i(아무 가방도 없는 경우)가 0인 경우 모두 0, j(최대 담을 수 있는 사이즈가 0인 경우)가 0인 경우도 모두 0의 값을 가진다.
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            # 담을 물건의 크기가 현재 담을 수 있는 크기보다 큰 경우
            if li[i - 1][0] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - li[i - 1][0]] + li[i - 1][1], dp[i - 1][j])

    result = dp[-1][-1]
    print(f'#{tc} {result}')


