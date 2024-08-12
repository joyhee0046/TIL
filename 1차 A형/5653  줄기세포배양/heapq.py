# 줄기세포 배양
import sys
sys.stdin = open('sample_input.txt')


import heapq

dxy = [[1, 0], [0, 1], [0, -1], [-1, 0]]
"""
heapq를 사용해서 생명력이 높은 친구가 먼저 번식하게 하고,
# 넣을 때 비교하는거 아니고, 높은걸 먼저 넣어서 자리가 차있으면 지나가기.

번식 위치를 저장하고 있는 변수에 미리 추가를 한다면,
이 후에 생명력이 낮은 친구는 해당 위치에 이미 번식이 되어 있기 때문에 번식을 못함 
"""
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    cell_set = set()
    activate = []  # 힙큐 리스트
    tmp = []

    # 초기 입력값 (생명력, 세로좌표, 가로좌표, 생성후시간) 으로 구조화하여 힙큐 및 방문지에 추가
    for n in range(N):
        for m in range(M):
            if grid[n][m] != 0:
                heapq.heappush(activate, (-grid[n][m], n, m, 0))
                cell_set.add((n, m))

    for _ in range(K):  # K시간 동안
        while activate:  # 살아있는 세포들 모두 검토
            x, cx, cy, t = heapq.heappop(activate)
            # 최대힙을 넣기 위해서 음수로 넣었기 때문에, 뺄 때 다시 음수를 곱해서 변환
            x = -x

            # 비활성화 -> t에 1 추가해서 다시 넣기
            if t < x:
                heapq.heappush(tmp, (-x, cx, cy, t+1))
                continue

            # 죽은 세포가 아닌 경우, 다시 목록에 추가
            if t + 1 < 2 * x:
                heapq.heappush(tmp, (-x, cx, cy, t + 1))

            # 분열해야하는 경우라면
            if x == t:
                for dx, dy in dxy:
                    nx, ny = cx + dx, cy + dy
                    # 이미 기존에 세포가 자리를 잡고 있다면
                    if (nx, ny) in cell_set: continue

                    heapq.heappush(tmp, (-x, nx, ny, 0))
                    # 생명력이 가장 높은 셀부터 처리하기 때문에 바로 자리를 차지해도 됨
                    # 이 후 같은 자리에 오려고 하는 세포가 나타나도
                    # 생명력이 더 적을 수 밖에 없기 대문에 괜찮음
                    ## 넣을 때 비교하는거 아니고, 높은걸 먼저 넣어서 자리가 차있으면 지나가기.
                    ## 최대힙으로 정렬되어있으니까.
                    cell_set.add((nx, ny))

        activate = tmp[:]
        tmp = []

    ans = len(activate)
    print(f'#{tc} {ans}')