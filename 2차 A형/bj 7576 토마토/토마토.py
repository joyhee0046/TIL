import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def toma_bfs(toma_box, queue):
    global day_cnt, same_day
    # 상하좌우 탐색
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if toma_box[nx][ny] != 0:
                continue
            queue.append((nx, ny))
            # 토마토에 날짜를 저장해서 불러오기
            toma_box[nx][ny] = toma_box[cx][cy]+1
    return toma_box
# 주어진 입력 받기
T = int(input())
for tc in range(1, 1+T):
    M, N = map(int, input().split())
    toma_box = [list(map(int, input().split())) for _ in range(N)]

    alr_toma = deque([])
    no_toma = []
    # 토마토 찾기
    for i in range(N):
        for j in range(M):
            if toma_box[i][j] == 1:
                alr_toma.append([i, j])
                continue
            if toma_box[i][j] == -1:
                no_toma.append([i, j])

    # 토마토 찾으러 가기
    toma_bfs(toma_box, alr_toma)
    print(max(map(max, toma_box))-1)