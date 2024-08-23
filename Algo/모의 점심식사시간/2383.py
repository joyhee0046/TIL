import sys
sys.stdin = open("sample_input.txt", "r")

import pprint

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

    # 사람 별로 필요 거리(시간) 찾기
    time = []
    cnt = 0
    for p_point in person_list:
        # 사람번호, 계단입구도착+1,내려가기
        time.append([[cnt, stair_list[0][2], moving_time(p_point, stair_list[0][0:2])+1],
                    [cnt, stair_list[1][2], moving_time(p_point, stair_list[1][0:2])+1]])
        cnt += 1
    # pprint.pprint(time)

    check_map = [False] * len(time)

