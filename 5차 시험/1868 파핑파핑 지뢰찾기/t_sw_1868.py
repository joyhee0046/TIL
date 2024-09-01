import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 지뢰찾기 크기
    arr = [list(input()) for _ in range(N)]  # 입력값
    res = 0  # 클릭 횟수 저장할 변수
    visited = [[False] * N for _ in range(N)]  # 방문 여부를 확인할 변수 초기화

    # 맵을 쫙 돌면서, 좌표별 주위에 폭탄 개수를 찾아준다.
    # 폭탄이 있는 위치는 방문하면 안되니까, 방문 처리를 해준다.
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '*':
                visited[i][j] = True
                continue
            # 좌표별 주위에 폭탄 개수를 찾아준다.
            # (i, j ) 주위 8방향에 대해서 폭탄이 몇 개 있는지를 찾는다.
            boom_cnt = 0
            for dx, dy in dxy:
                ni, nj = i + dx, j + dy
                # 범위 검사
                if 0 > ni or ni >= N or 0 > nj or nj >= N: continue
                if arr[ni][nj] == '*':
                    boom_cnt += 1
            arr[i][j] =boom_cnt

    # 좌표 하나하나를 다 클릭해본다.
    # 클릭한 부분이 주변에 폭탄이 없으면, 다시 8방으로 탐색해서 큐에 집어넣고
    # 큐가 빌 때까지 위 과정을 반복한다.
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0: continue  # 주변에 폭탄이 있는 경우면 continue
            if visited[i][j]: continue  # 방문한 적있으면 누를 필요가 없죠
            # 빈칸만 누를거에요.
            queue = deque([(i, j)])
            visited[i][j] = True
            while queue:
                ci, cj = queue.popleft()

                # 주변에 폭탄이 존재한다면 터트리지 않음
                if arr[ci][cj] != 0: continue
                for dx, dy in dxy:
                    ni, nj = ci + dx, cj + dy
                    if 0 > ni or ni >= N or 0 > nj or nj >= N: continue
                    if arr[ni][nj] == '*': continue  # 폭탄이면 큐에 넣지 않고 continue
                    if visited[ni][nj]: continue

                    visited[ni][nj] = True
                    # if arr[ni][nj] != 0: continue
                    queue.append((ni, nj))
            res += 1

    # 여기가 어쩌면 엣지 케이스일 수도 있다.
    # 우리가 하나한 눌러줘야하는 숫자들밖에 안남았다
    # 빈칸은 연쇄작용으로 다 터졌다.
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:  # 폭탄은 방문처리, 빈칸도 방문처리 , 방문처리 X => 숫자
                res += 1

    print(f"#{test_case} {res}")