'''오답
채점용 input 파일로 채점한 결과 fail 입니다.
(오답 : 20개의 테스트케이스 중 5개가 맞았습니다.)

제한시간 초과가 발생하였습니다. 제한시간 초과로 전체 혹은 일부 테스트 케이스는 채점이 되지 않을 수 있습니다.'''

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
            if
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
    # 모든 칸 확인하기, 물에서 탐색 시작
    for i in range(N):
        for j in range(M):
            if summer_map[i][j] == 'W':
                check_map[i][j] = 0
                queue.append((i, j))
                visit_map = [[False] * M for _ in range(N)]
                continue
    find_land(check_map)

    ans = 0
    for i in range(N):
        for j in range(M):
            ans += check_map[i][j]

    print(f'#{tc} {ans}')