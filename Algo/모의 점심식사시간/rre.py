import sys
sys.stdin = open("sample_input.txt", "r")

# 계단까지 올라가기
def moving_time(p_point, st_point):
    return abs(p_point[0] - st_point[0]) + abs(p_point[1] - st_point[1])

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stairs_map = [list(map(int, input().split())) for _ in range(N)]

    # 시작 위치 모으기
    stair_list = []
    person_list = []
    for i in range(N):
        for j in range(N):
            if stairs_map[i][j] == 0:
                continue
            if stairs_map[i][j] == 1:
                person_list.append([i,j])
                continue
            stair_list.append([i,j,stairs_map[i][j]])

    # 사람 별로 최소 거리 찾기
    time = []
    for p_point in person_list:
        temp = []
        cnt = 0
        for st_point in stair_list:
            cnt += 1
            temp.append([moving_time(p_point, st_point[0:2]), cnt])
        time.append(min(temp))

    order_list = dict()
    for t, s in time:
        if t in order_list:
            order_list[t].append(s)
            continue
        order_list[t] = [s]
    
    

    # 시간과 계단이 겹치면 다른 길 탐색해보기