import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dxy = [[1, 0], [0, 1], [0, -1], [-1, 0]]

# 주어진 입력 받기
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]
    # 살아있는 세포 activate, 죽은 친구를 없애기 위한 deque
    activate = deque()
    # 살아있는 세포들을 큐에 넣어서, bfs 탐색을 진행
    for n in range(N):
        for m in range(M):
            # 죽었으면 pass, 얼리리턴
            if grid[n][m] == 0: continue
            # 생명력, 위치 좌표 i, 좌표 j,살아있는 시간
            activate.append([grid[n][m], n, m, 0])

    # 셀이 존재하는 좌표를 저장
    cell_set = set()
    # k 시간동안 세포 분열 진행
    for k in range(K):
        # 분열하는 세포를 임시로 저장할 변수
        tmp_activate = []
        # 분열하는 세포들을 저장할 좌표 ( key: 좌표, value: [], 생명력이 값으로 들어감  )
        spread_cell_dict = {}
        # 이번 k time 때 증식해야 하는 세포
        # 살아있는 세포가 남아있다면 계속 반복
        while activate:
            x, cx, cy, t = activate.pop()
            # 현재 좌표를 추가_기존에 누가 앉아있다면 늘어나지 않음.
            cell_set.add((cx, cy))

            # 비활성화 -> 활성화
            if t < x:
                tmp_activate.append([x, cx, cy, t + 1])
                continue

            # 분열해야 하는 경우
            if t == x:
                # 델타 탐색
                for dx, dy in dxy:
                    nx, ny = cx + dx, cy + dy

                    # 분열할 위치가 이미 기존의 세포가 차지하고 있던 경우
                    if (nx, ny) in cell_set: continue

                    # 생명력 수치가 가장 높은 세포를 얻기 위해서 동일하게 분열하는 세포들을 모으기
                    spread_cell_dict.setdefault((nx, ny), []).append(x)

            # 죽은 세포가 아니라면
            # 분열 후 기존 세포에 시간을 추가해서 다시 activate에 추가
            ## 2x로 볼 수도 있지만 -1을 할 수도 있음.
            if t + 1 < 2 * x:
                tmp_activate.append([x, cx, cy, t + 1])

        # tmp_activate에서 중복 셀 제거 작업 진행 후 다시 activate에 집어넣기
        activate = tmp_activate[:]
        # key: 위치, value : cell 생명력 리스트
        for cell_pos, x_list in spread_cell_dict.items():
            # 기존에 넣은 것처럼 현재 좌표에 번식된 세포들 중 가장 생명력이 높은 값, 위치, 시간은 0
            activate.append([max(x_list), cell_pos[0], cell_pos[1], 0])

    print(f"#{test_case} {len(activate)}")
