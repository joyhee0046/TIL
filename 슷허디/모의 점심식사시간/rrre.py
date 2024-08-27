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
    # [[0, 3, 5], [0, 5, 6], [1, 3, 4], [1, 5, 5], [2, 3, 3], [2, 5, 4], [3, 3, 5], [3, 5, 4], [4, 3, 3], [4, 5, 4], [5, 3, 8], [5, 5, 3]]

    # time[i][0]값이 겹치지 않도록 각 1가지씩 선택해하는 재귀 돌기
    ## 각 사람이 1로갈 경우/2로갈 경우

    result = 0

    def dfs(pick, stair_1, stair_2):  # 이번에 출발할 사람/왼쪽시간/오른쪽시간
        global result

        for i in range(len(time)):
            # 지나간 사람 넘어가기
            if check_map[i]:
                continue
            # 사용했다고 체크해주기
            check_map[i] = True

            # 1번계단으로 가기
            dfs(pick + 1, stair_1.append(time[i][0], stair_2)

            if time[i][2] in stair_2:
                continue

            # 2번계단으로 가기
            dfs(pick + 1, stair_1, stair_2 + arr[i])
            # 원복
            check_map[i] = False
        result = min(stair_1, stair_2)

    dfs(0, [], [])