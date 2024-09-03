'''
오답
채점용 input 파일로 채점한 결과 fail 입니다.
(오답 : 20개의 테스트케이스 중 2개가 맞았습니다.)

제한시간 초과가 발생하였습니다. 제한시간 초과로 전체 혹은 일부 테스트 케이스는 채점이 되지 않을 수 있습니다.
'''

import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque
def find_land(map):
    while queue:
        cx, cy = queue.popleft()
        visit_map[cx][cy] = True
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            # 범위 벗어나면 지나가기
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 확인했던 곳이면 지나가기
            if visit_map[nx][ny]:
                continue
            # 물이면 지나가기
            if summer_map[nx][ny] == "W":
                continue
            # 아까보다 한 칸 더 온걸로 거리 저장
            check_map[nx][ny] = check_map[cx][cy]+1
            # 방문처리
            visit_map[nx][ny] = True
            # 다음으로 이동하기 위해서 큐에 저장
            if (nx, ny) in queue:
                continue
            queue.append((nx, ny))
    return check_map

# 사방탐색
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
                visit_map[i][j] = True
                continue
    find_land(check_map)

    ans = 0
    for i in range(N):
        for j in range(M):
            ans += check_map[i][j]

    print(f'#{tc} {ans}')