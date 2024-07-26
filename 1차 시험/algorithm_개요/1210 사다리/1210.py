# input 파일 읽기
import sys
sys.stdin = open("input.txt", "r")

# # 테스트케이스 10번 반복
# for _ in range(10):
#     tc = int(input())
#     board = [list(map(int, input().split())) for _ in range(100)]
#     j = 0
#     # 최하단 왼쪽부터 목표지점인 2가 어느 위치에 있는지 확인. point에 2인 좌표 저장. x축 j에 저장
#     for i in range(100):
#         point = board[99][i]
#         if point == 2:
#             ans = i
#     # 목표지점에서 출발해서 위로 경로 탐색
#     j = ans
#     x = 98
#     board[x][j] = 0
#     while x != 0:
#         if board[x][j-1] == 1:
#             board[x][j-1] = 0
#             j -= 1
#         elif board[x][j+1] == 1:
#             board[x][j + 1] = 0
#             j += 1
#         elif board[x-1][j] == 1:
#             board[x - 1][j] = 0
#             x -= 1
#     print(f"#{tc} {j}")



dxy = [[-1,0], [0, -1], [0, 1]]

def search_leader(x, y):
    data[x][y] = 0

    while x != 0:
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny]:
                data[x][y] = 0
                x, y = nx, ny
    return y

for _ in range(10):
    tc = int(input())
    result = -1  # 찾지 못하면 -1
    data = [list(map(int, input().split())) for _ in range(100)]

    # 도착점부터 시작하자
    # 도착점은 항상 99 번째 줄에 있겠죠
    for j in range(100):
        if data[99][j] == 2:
            result = search_leader(99, j)  # 어차피 답은 한 개거든요
            break
    print(f"#{tc} {result}")