import sys
sys.stdin = open("input.txt", "r")

for i in range(10) :
    tc = int(input())
    board = [list(map(int,input().split())) for _ in range(100)]
    for i in range(100) :
        point = board[0][i]
        if point == 1 :
            j = i
            n = 0
            while point !=0 :
                n += 1
                point = board[n][j]
                if n == 100 :
                    break

                if point == 2 :
                    print(i)