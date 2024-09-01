import sys
sys.stdin = open('sample_input.txt')

from collections import deque
from copy import deepcopy

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# BFS를 사용한 벽 지우기 시뮬레이션
def cal_wall(board, start_y, start_x):
    c_board = deepcopy(board)
    next_board = [[0] * len(board[0]) for _ in range(len(board))]
    # 큐 도는 동안 c_board 배열 손상시키기
    queue = deque([])
    queue.append((start_y, start_x, c_board[start_y][start_x]))
    c_board[start_y][start_x] = 0
    while queue:
        y, x, cnt = queue.popleft()
        # 2면 +1만 터져야하고, 3이어야 +1, +2가 터지기 때문
        for pos in range(1, cnt):
            for i in range(4):
                ny = y + dy[i] * pos
                nx = x + dx[i] * pos
                if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]):
                    continue
                if c_board[ny][nx] == 0:
                    continue
                queue.append((ny, nx, c_board[ny][nx]))
                c_board[ny][nx] = 0
    for idx_x in range(len(board[0])):
        cur_y = len(board) - 1
        for idx_y in range(len(board)):
            if c_board[len(board) - idx_y - 1][idx_x] != 0:
                next_board[cur_y][idx_x] = c_board[len(board) - idx_y - 1][idx_x]
                cur_y -= 1
    return next_board


# DFS를 사용한 공던지기 시뮬레이션
def try_ball(board, num, size_x, size_y):
    global min_cnt
    if num == 0:
        # 세고
        cnt = 0
        for li in board:
            for elem in li:
                if elem != 0:
                    cnt += 1
        min_cnt = min(min_cnt, cnt)
        return
    # 끝까지 오기 전에 다 깨진 경우
    if sum(board[size_y - 1]) == 0:
        min_cnt = 0
        return
    for start_x in range(size_x):
        # y좌표 찾기. 없으면 반환하기.
        start_y = -1
        for idx in range(size_y):
            if board[idx][start_x] != 0:
                # print(board[idx][start_x])
                start_y = idx
                break
        # 해당 줄에 공이 없을 때
        if start_y == -1:
            continue
        # 해당 좌표롤 기준으로 부순 board 반환받고
        result_board = cal_wall(board, start_y, start_x)
        try_ball(result_board, num - 1, size_x, size_y)



T = int(input())
for tc in range(1, T + 1):
    min_cnt = float("inf")
    num, size_x, size_y = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(size_y)]

    try_ball(board, num, size_x, size_y)

    print(f"#{tc} {min_cnt}")