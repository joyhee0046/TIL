import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]
    cnt = N-X
    diff_x = ground[0][0]
    diff_y = ground[0][0]
    for i in range(N-X):
        for j in range(N-X):
            if diff_x - ground[i][j] > 1 :
                continue
            if ground[i][j] == ground[i][j:j+X] :

            if abs(test1 - ground[i][j]) <= 1 :
                test 1 = ground[i][j]
            ground[j][i]