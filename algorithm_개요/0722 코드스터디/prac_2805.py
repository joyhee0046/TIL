import sys
sys.stdin = open('input_2805.txt','r')

T = int(input())

for test_case in range(1,T + 1):
    N = int(input())
    crop = [list(map(int,input().rstrip()))for _ in range(N)]
    ans = 0
    for i in range(N):
        range_ = abs(N//2 - i)
        ans += sum(crop[i][range_:N-range_])
    print(f'#{test_case} {ans}')