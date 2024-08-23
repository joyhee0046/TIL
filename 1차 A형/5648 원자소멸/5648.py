import sys
sys.stdin = open("sample_input.txt", "r")


def sec_move(ans, check, l_sec):

    for i in range(N):
        nx, ny = xli[i]+wayli[i][0], yli[i]+wayli[i][1]
        this_sec = []

        if check[nx][ny] == 0:
            check[nx][ny] = i
            this_sec.append([nx, ny])

        if check[nx][ny] != 0:
            ans += kli[check[nx][ny]]
            ans += kli[i]

    for i in range(len(l_sec)):
        check[l_sec[i]] = 0
    l_sec = this_sec[:]

    sec_move(ans, check, l_sec)





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

    check = [[0]*(max(xli)+1)] * (max(yli)+1)
    for i in range(N):
        check[xli[i]][yli[i]] = i

    ans = 0

    l_sec = []

    sec_move(ans, check, l_sec)


# import sys
# sys.stdin = open("sample_input.txt", "r")
#
#
# def move(board, ans):
#     dxy = [[0, 1000], [0, -1000], [-1000, 0], [1000, 0]]
#     zipxy = []
#     check[board[i][0], board[i][1]] = 1
#
#     for i in range(len(board)):
#         nx, ny = dxy[board[i][2]][0] + board[i][0], dxy[board[i][2]][1] + board[i][1]
#         check[board[i][0]:nx][:] = 2
#         check[board[i][1]:ny][:] = 2
#         if
#
#     # for i in range(len(zipxy)):
#     #     if
#     print(zipxy)
#
#
# T = int(input())
# for tc in range(1, 1 + T):
#     N = int(input())
#     board = []
#     for _ in range(N):
#         x, y, w, k = map(int, input().split())
#         board.append([x, y, w, k])  # 원소별 특징을 리스트로 저장. 특징2인 방향은 인덱스로 활용
#     check = [[0] * 1000] * 1000
#     ans = 0
#     move(board, ans)