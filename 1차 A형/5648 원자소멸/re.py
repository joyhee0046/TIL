import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    xli = []
    yli = []
    wayli = []
    kli = []
    for _ in range(N):
        x, y, w, k = map(int, input().split())
        xli.append(x)
        yli.append(y)
        wayli.append(w)
        kli.append(k)

    for i in range(N):
        if wayli[i] == 0:
            wayli[i] = [0, 1]
        if wayli[i] == 1:
            wayli[i] = [0, -1]
        if wayli[i] == 2:
            wayli[i] = [-1, 0]
        if wayli[i] == 3:
            wayli[i] = [1, 0]

    moveli = []
    for i in range(N):
        moveli.append(str([xli[i],yli[i]]))



    for i in range(N):
        moveli.insert(i*2+1, str([wayli[i][0] + xli[i], wayli[i][1] + yli[i]]))
    print(moveli)

    if len(moveli) != len(set(moveli)):
        pass

    for i in range(N):
        moveli.pop((N-i-1)*2)

    print(moveli)