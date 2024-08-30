import sys
sys.stdin = open('re_sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    xli = list(map(int, input().split()))
    yli = list(map(int, input().split()))
    E = int(input())

    lli = [0 for _ in range(N)]
    tt_l = {}
    for i in range(N):
        tt_l[i] = ''
        for j in range(N):
            tt_l[i] = (j, ((xli[i] - xli[j])**2 + (yli[i] - yli[j])**2))

