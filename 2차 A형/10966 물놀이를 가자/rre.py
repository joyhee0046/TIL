import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque
def find_land(map):

    while queue:
        cx, cy = queue.popleft()
        visit_map[cx][cy] = True
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visit_map[nx][ny]:
                continue
            if summer_map[nx][ny] == "W":
                continue
            check_map[nx][ny] = check_map[cx][cy]+1
            visit_map[nx][ny] = True
            queue.append((nx, ny))
    return check_map

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    summer_map = [list(input()) for _ in range(N)]

    check_map = [[999999] * M for _ in range(N)]

    queue = deque([])
    # water_spot = []
    # land_spot = []
    # 모든 칸 확인하기, 땅이 어디고 물이 어딘지
    for i in range(N):
        for j in range(M):
            if summer_map[i][j] == 'W':
                # water_spot.append((i, j))
                check_map[i][j] = 0
                queue.append((i, j))
                visit_map = [[False] * M for _ in range(N)]
                visit_map[i][j] = True

                continue
            # land_spot.append((i, j))
    find_land(check_map)
    # for x, y in water_spot:
    #     dist = 0
    #     find_land(check_map, x, y)

    print(summer_map, visit_map, check_map)  # 섬의 개수 출력
    print(f'#{tc} {sum(sum(check_map, []))}')