import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    # dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    # li[i][0]을 잘 골라서
    # li[i][1]을 최대로
    dp = [0] * (N+1)

    for j in range(N):
        s, p = li[j][0], li[j][1]
        if N < N-j-s:
            continue
        for i in range(j, j+s+1):
            if dp[i] < dp[s+i]+p:
                dp[i] = dp[s+i]+p

    print(f"#{max(dp)}")