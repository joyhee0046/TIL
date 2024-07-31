import sys
sys.stdin = open("sample_input.txt", 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    for K in range(2, (N//2)+2):
        cost = K * K + (K - 1) * (K - 1)
        print(cost)

        area = K*2-1

        # li에서 대각K*K로 범위 잡기
        for i in range(N):
            for j in range(i, area):

                if i >= N // 2:
                    j += 1
                    k -= 1
                else:
                    j -= 1
                    k += 1

