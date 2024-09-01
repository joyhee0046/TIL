import sys
sys.stdin = open("input.txt", "r")

from collections import deque
dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    borad = [list(input()) for _ in range(N)]
    ans = 0
    borad_check = [[0] * N for _ in range(N)]

    # 맵을 쫙 돌면서, 좌표별 주위에 폭탄 개수를 찾아준다.
    # 폭탄이 있는 위치는 방문하면 안되니까, 방문 처리를 해준다.
    for i in range(N):
        for j in range(N):
            # 지뢰 먼저 찾아서 방문처리. 탐색 중에 지뢰를 누르지 못하게
            if borad[i][j] == '*':
                borad_check[i][j] = 2
                continue
            # 선택된 자리를 기준으로 8방에 지뢰가 있는지 확인해주기
            # 선택+8방해서 9곳에 지뢰가 없다면 재귀, 옆자리도 지뢰가 없는지 확인해야 함.
            boom_cnt = 0
            for dx, dy in dxy:
                ni, nj = i + dx, j + dy
                # 보드판을 벗어나면 넘어가기
                if 0 > ni or ni >= N or 0 > nj or nj >= N: continue
                # 지뢰면 카운트 올리기
                if borad[ni][nj] == '*':
                    borad_check[i][j] = 1
                    break

    # 완탐할건데, 9자리에 폭탄 없으면 재귀_큐에 넣어서
    for i in range(N):
        for j in range(N):
            # 주변에 폭탄이 있으면 넘어가기
            if borad_check[i][j] != 0: continue
            # 확인해야 하는 자리 큐에 넣고
            queue = deque([(i, j)])
            # 방문처리
            borad_check[i][j] = 1
            # 큐가 비어있지 않다면 계속 실행
            while queue:
                # 확인할 좌표 뽑아주고
                ci, cj = queue.popleft()
                # 주변에 폭탄이 있다면 넘어가기
                if borad_check[ci][cj] != 0: continue
                # 8방 탐색
                for dx, dy in dxy:
                    ni, nj = ci + dx, cj + dy
                    # 보드판 범위를 벗어난다면 넘어가기
                    if 0 > ni or ni >= N or 0 > nj or nj >= N: continue
                    # 폭탄이면 넘어가기
                    if borad[ni][nj] == '*': continue
                    # 방문했던 곳이면 넘어가기
                    if borad_check[ni][nj] != 0: continue
                    # 맨땅이라면 방문체크하고 큐에 넣기_한 덩어리로 터질 수 있는 옆칸 확인용 재귀
                    borad_check[ni][nj] = 1
                    queue.append((ni, nj))
            # 정답 카운트 하나 올리기
            ans += 1

    # 방문처리 되지 않은 칸 하나씩 눌러주기
    for i in range(N):
        for j in range(N):
            if borad_check[i][j] != 0:
                ans += 1

    # 정답 출력
    print(f"#{test_case} {ans}")