from collections import deque

# 상, 하, 좌, 우 방향을 나타내는 리스트 (dxy)
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def move():
    global ans
    # 큐에 (x, y, h, f) 튜플 삽입
    # (x, y)는 현재 위치, h는 현재 위치의 높이, f는 현재까지 소모한 연료
    queue = deque([(0, 0, arr[0][0], 0)])

    # 큐가 빌 때까지 반복
    while queue:
        x, y, h, f = queue.popleft()  # 큐에서 하나씩 꺼냄

        # 목적지 (n-1, n-1)에 도달했다면, 최소 연료를 기록하고 계속 진행
        if x == n - 1 and y == n - 1:
            ans = min(ans, f)
            continue

        # 상, 하, 좌, 우 네 방향으로 이동 시도
        for m in dxy:
            nx, ny = x + m[0], y + m[1]

            # 범위 체크와 연료가 더 적게 드는 경로만 진행
            if 0 <= nx < n and 0 <= ny < n and fuel[nx][ny] > f:
                # 이동하려는 칸이 현재 높이보다 낮으면 연료 추가 안 함
                if h > arr[nx][ny]:
                    nf = f  # 낮은 곳으로 이동 시 연료 0
                # 현재 높이와 이동하려는 칸의 높이가 같으면 연료 1 소모
                elif h == arr[nx][ny]:
                    nf = f + 1  # 같은 높이로 이동 시 연료 1
                # 이동하려는 칸의 높이가 더 높으면 차이 * 2만큼 연료 소모
                else:
                    nf = f + (arr[nx][ny] - h) * 2  # 높은 곳으로 이동 시 연료 차이 * 2

                # 새로운 위치에서 더 적은 연료로 도달할 수 있으면 갱신
                fuel[nx][ny] = nf
                # 큐에 새로운 위치와 연료 정보를 넣음
                queue.append((nx, ny, arr[nx][ny], nf))

# 테스트 케이스 수 입력
T = int(input())

# 각 테스트 케이스마다 처리
for tc in range(T):
    # 산의 크기 N 입력
    n = int(input())
    # 산의 높이를 2D 배열로 입력
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 최소 연료를 저장할 변수 초기화 (무한대로 설정)
    ans = float('inf')

    # 각 칸에 대한 최소 연료를 저장할 배열 초기화 (모든 칸을 무한대로 설정)
    fuel = [[float('inf')] * n for _ in range(n)]
    # 시작점 (0, 0)의 연료는 0
    fuel[0][0] = 0

    # 이동 함수 실행
    move()

    # 각 테스트 케이스에 대해 결과 출력
    print(f'#{tc + 1}', ans)
