import sys
sys.stdin = open('sample_input(1).txt', 'r')


def fibo_dp(n):
    if n <= 3:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 6
    for i in range(4, n + 1):
        dp[i] = dp[i-1] + (dp[i-2] * 2) + dp[i-3]
    return dp[n]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {fibo_dp(N)}')