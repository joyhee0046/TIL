import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for _ in range(T):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    # li.reverse()
    # li.insert(0, [])
    # # print(li)
    # # dp 테이블 초기화
    # d = [0] * (N + 1) # DP 배열 또한 인덱스를 날짜로 사용하기 위해 길이를 1 증가
    # for i in range(1, N + 1):
    #     if i < li[i][0]:
    #         d[i] = d[i - 1]
    #     else:
    #         d[i] = max(d[i - 1], li[i][1] + d[i - li[i][0]])
    # print(d[N])


N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for i in range(N+1)]
for i in range(N):
    for j in range(i+li[i][0], N+1):
        if dp[j] < dp[i] + li[i][1]:
            dp[j] = dp[i] + li[i][1]
print(dp[-1])
