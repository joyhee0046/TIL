import sys
sys.stdin = open("sample_input (1).txt", "r")


# 두 좌표간의 거리를 구하는 함수
def get_dis(a_pos, b_pos):
    return abs(a_pos[0] - b_pos[0]) + abs(a_pos[1] - b_pos[1])


"""
1. 시간에 따라 각 사용자들을 이동시키고 

2. 사용자 기준으로 접속한 AP 목록을 수집 

3.1. a 사용자와 연결된 경우에 충전
3.2  b 사용자와 연결된 경우에 충전
3.3 ==-> 사용자 a, b 둘다 연결된 경우에는?  ( 이미 위에서 3.1/ 3.2를 처리했다면? )
==> 그래서 a만 연결 / b만 연결 / a,b 동시 연결 나눠야한다. 

"""
# 정지, 상, 우, 하, 좌
dxy = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    a_mv_list = list(map(int, input().split()))
    b_mv_list = list(map(int, input().split()))
    ap_list = [list(map(int, input().split())) for _ in range(A)]
    A_START_POS, B_START_POS = 1, 10
    ax, ay = A_START_POS, A_START_POS
    bx, by = B_START_POS, B_START_POS

    # 충전량의 합을 저장할 변수
    result = 0

    # 주어진 시간동안 이동하면서 충전량의 합을 구하기
    for t in range(M + 1):
        # a 사용자, b 사용자 범위에 들어온 ap를 저장할 목록
        a_connects, b_connects = [], []

        # 모든 ap 목록에 대해서 범위에 포함되는 ap를 a 사용자 범위에 추가함
        for ap in ap_list:
            # ap 위치, 충전 범위, 충전 파워
            ap_x, ap_y, c, p = ap[0], ap[1], ap[2], ap[3]

            # 사용자 a의 위치와 ap의 위치가 범위 안에 든다면 연결점에 추가
            if get_dis([ax, ay], [ap_x, ap_y]) <= c:
                a_connects.append([[ap_x, ap_y], p])
            if get_dis([bx, by], [ap_x, ap_y]) <= c:
                b_connects.append([[ap_x, ap_y], p])

        power_max = 0
        # a만 근처에 ap가 있는 경우
        if a_connects and not b_connects:
            # a와 근처에 있는 ap 중 가장 파워가 쎈 ap로 충전
            # 여러 ap 범위에 있다면, 문제에서 가장 많이 충전했을 때를 구해야함으로
            # 가장 큰 ap로 충전한다.
            for a_connect_ap in a_connects:
                power_max = max(power_max, a_connect_ap[1])

        # b에만 속해 있는 경우
        elif b_connects and not a_connects:
            for b_connect_ap in b_connects:
                power_max = max(power_max, b_connect_ap[1])

        # a와 b 모두에 속해있는 경우
        else:
            # 나올 수 있는 모든 경우의 수 확인
            for a_connect_ap in a_connects:
                for b_connect_ap in b_connects:
                    # 똑같은 ap에 접속하는 경우, 절반씩 나눠가지므로
                    # 충전되는 양은 ap 한 개 충전량을 해당 시간의 충전량으로 함
                    if a_connect_ap[0] == b_connect_ap[0]:
                        power_max = max(power_max, a_connect_ap[1])
                    # 서로 다른 ap일 경우에는 2개의 ap 충전량의 합을 해당 시간의 충전량
                    else:
                        power_max = max(power_max, a_connect_ap[1] + b_connect_ap[1])

        result += power_max

        # M 시간을 소요하면 더 이상 이동하지 않기 위해서 중단
        if t == M:
            break

        # 주어진 시간에 해당하는 방향으로 이동
        ax += dxy[a_mv_list[t]][0]
        ay += dxy[a_mv_list[t]][1]
        bx += dxy[b_mv_list[t]][0]
        by += dxy[b_mv_list[t]][1]

    print(f"#{test_case} {result}")