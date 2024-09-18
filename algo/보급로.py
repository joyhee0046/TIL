import sys
sys.stdin = open('2_input.txt', 'r')

from collections import deque

# 메인 함수
def restore_road(road, N):
    # 사방탐색
    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # 출발지가 들어있는 큐 만들기
    queue = deque([(0, 0)])
    # 방문확인할 배열 만들기
    chek_time = [[9999 for _ in range(N)] for _ in range(N)]
    # 출발 위치 처리
    chek_time[0][0] = 0
    # 큐가 빌 때까지
    while queue:
        # 첫번째 요소꺼내서 x,y에 담기
        x, y = queue.popleft()
        # 사방탐색 시작
        for dir in dxy:
            nx = x + dir[0]
            ny = y + dir[1]
            # 배열 범위를 벗어난다면 지나가기
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue
            # 지금까지 지나온 시간 + 나아갈 방향의 시간 더해서 저장
            new_time = chek_time[x][y] + road[nx][ny]
            # 새로 계산한 시간이 저장되어 있는 시간보다 작다면
            if new_time < chek_time[nx][ny]:
                # 시간 값 갱신
                chek_time[nx][ny] = new_time
                # 큐에 추가해서 탐색 들어가기
                queue.append([nx, ny])
    # 도착지 값 반환
    return chek_time[-1][-1]

# 주어진 입력 받기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]
    # 메인 함수 실행
    ans = restore_road(road, N)
    # 정답 출력
    print(f"#{tc} {ans}")