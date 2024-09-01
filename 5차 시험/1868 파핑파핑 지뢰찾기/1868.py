import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for i in range(N)]
    arr_ch = [[0 for i in range(N)] for i in range(N)]
    count = 0

    dpcol = [0, -1, 0, 1, 0, 1, -1, -1, 1]
    dprow = [0, 0, 1, 0, -1, 1, 1, -1, -1]

    for col in range(N):
        for row in range(N):
            if arr_ch[col][row] == 0:
                if arr[col][row] == '*':
                    arr_ch[col][row] = 2
                else:
                    check = 0
                    right = 0
                    for v in range(9):
                        ncol = col + dpcol[v]
                        nrow = row + dprow[v]
                        if 0 <= ncol < N and 0 <= nrow < N:
                            if arr_ch[ncol][nrow] == 0:
                                if arr[ncol][nrow] == '.':
                                    check += 1
                                    right += 1
                                else:
                                    right += 1
                            if arr_ch[ncol][nrow] == 2:
                                right += 1
                    # print(right, check)
                    if check == right:
                        count += 1
                        for v in range(9):
                            ncol = col + dpcol[v]
                            nrow = row + dprow[v]
                            if 0 <= ncol < N and 0 <= nrow < N:
                                arr_ch[ncol][nrow] = 1

    for col in range(N):
        for row in range(N):
            if arr_ch[col][row] == 0:
                count += 1

    print(f'#{test_case} {count}')

## 지금은 한바퀴만 검사할 수 있음.  공간 넓힐수 있도록 재귀돌아야.
