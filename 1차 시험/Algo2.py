import sys
sys.stdin = open("algo2_sample_in.txt", "r")
# 데이터 전송경로
# 네트워크는 미로로 표현된다. 데이터 패킷은 상하좌우로 이동할 수 있고, 벽에 부딪힐 때까지 멈추지 않는다.
# 최단 거리를 구해라.

T = int(input())  # 테스트케이스 수 입력받기
for tc in range(1, T+1):  # 테스트케이스만큼 반복
    M, N = map(int, input().split())  # 네트워크 행렬 받기
    road = []  # 네트워크를 넣을 빈 리스트
    for _ in range(M):   # M번 반복하여 M줄 입력받기
        road.append(list(map(int, input().split()))) # 네트워크 리스트에 네트워크 추가
    Si, Sj, Di, Dj = map(int, input().split())  # 시작위치와 목적위치 입력받기

    check_road = [[9999]*N for _ in range(M)]  # 지나간 길을 확인할 리스트
    x = Si
    y = Sj
    end = [Di, Dj]
    dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 상하좌우 이동값을 줄 리스트
    check_road[x][y] = 0  # 시작점에 0번 이동했다고 체크해주기

    def move(road, x, y):
        for dx, dy in dxy:
            nx = x + dx  # 이동예정 x인덱스
            ny = y + dy  # 이동예정 y인덱스
            if 0 > nx or M <= nx or 0 > ny or N <= ny:  # 이동 예정 지점이 네트워크지도를 벗어나는지 확인
                continue  # 벗어난다면 skip
            if road[nx][ny] == 1:  # 이동 예정 지점이 네트워크 지도상 벽인지 확인
                continue  # 벽이라면 skip
            if check_road[nx][ny] < check_road[x][y] + 1:  # 이동 예정 지점에 또 가야 하는지 확인
                continue
            check_road[nx][ny] = check_road[x][y] + 1  # 이동해야 한다면 기존의 이동횟수+1을 이동지점에 저장
            while True:
                keep_x = nx + dx  # 계속해서 이동할 x방향
                keep_y = ny + dy  # 계속해서 이동할 y방향
                if 0 > keep_x or M <= keep_x or 0 > keep_y or N <= keep_y:  # 패킷이 벽에 부딪혔다면
                    x = nx  # 벽에 만나기 직전 값을 x로 저장
                    y = ny  # 벽에 만나기 직전 값을 y로 저장
                    False
                    break
                if road[keep_x][keep_y] == 1:  # 패킷이 벽에 부딪혔다면
                    x = nx  # 벽에 만나기 직전 값을 x로 저장
                    y = ny  # 벽에 만나기 직전 값을 y로 저장
                    False
                    break
                check_road[keep_x][keep_y] = check_road[nx][ny] + 1   # 아직 패킷이 직진해야하니까
                nx = keep_x  # nx바꿔주고
                ny = keep_y  # ny도 바꿔주기
        # if x == Di and y == Dj:
        #     move(road, x, y)

        #print(check_road)

    move(road, Si, Sj)

    if check_road[Di][Dj] == 9999:
        ans = -1
    else:
        ans = check_road[Di][Dj]

    print(f"#{tc} {ans}")



