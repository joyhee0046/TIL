import sys
sys.stdin = open("../../../Downloads/sample_input (8).txt", "r")
from collections import deque


def get_dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def down_stairs(stair_on_list):
    for idx in range(MAX_PEOPLE_ON_STAIRS):
        if stair_on_list[idx] != 0:
            stair_on_list[idx] -= 1
    return stair_on_list


def place_people_on_stairs(waiting_queue, stair_on_list, stair_len, cnt_time):
    for stair_idx in range(MAX_PEOPLE_ON_STAIRS):
        if waiting_queue and waiting_queue[0] <= cnt_time and stair_on_list[stair_idx] == 0:
            pop_data = waiting_queue.popleft()
            if pop_data == cnt_time:
                stair_on_list[stair_idx] = stair_len + 1
            else:
                stair_on_list[stair_idx] = stair_len
    return


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    MAX_PEOPLE_ON_STAIRS = 3
    min_time = 999999

    people_list = []  # 사람들 위치
    stair_list = []  # 계단 위치
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0:
                continue
            elif maps[i][j] == 1:
                people_list.append([i, j])
            else:
                stair_list.append([i, j, maps[i][j]])


    def dfs(idx, a_dist_list, b_dist_list):
        global min_time

        # a 입구로 도착한 사람들이 존재하고,
        # 현재까지 최소 거리보다, 가장 늦게 도착한 사람 + 계단 길이인 경우에는 아래 로직을 계산하지 않음
        if a_dist_list and min_time <= max(a_dist_list) + stair_list[0][2]:
            return
        if b_dist_list and min_time <= max(b_dist_list) + stair_list[1][2]:
            return

        if idx == len(people_list):
            # queue 구현해서 최종 시간에 따라 최소시간 갱신하기
            t = 0
            a_stair_on_list = [0] * MAX_PEOPLE_ON_STAIRS
            b_stair_on_list = [0] * MAX_PEOPLE_ON_STAIRS

            a_dist_list.sort()
            b_dist_list.sort()

            a_queue = deque(a_dist_list)
            b_queue = deque(b_dist_list)
            while True:

                a_stair_on_list = down_stairs(a_stair_on_list)
                b_stair_on_list = down_stairs(b_stair_on_list)

                place_people_on_stairs(a_queue, a_stair_on_list, stair_list[0][2], t)
                place_people_on_stairs(b_queue, b_stair_on_list, stair_list[1][2], t)

                if not a_queue and not b_queue and sum(a_stair_on_list) == 0 and sum(b_stair_on_list) == 0:
                    break

                t += 1
                if min_time <= t:
                    return

            min_time = min(min_time, t)
            return

        a_dist = get_dis(stair_list[0][:2], people_list[idx])
        dfs(idx + 1, a_dist_list + [a_dist], b_dist_list)

        b_dist = get_dis(stair_list[1][:2], people_list[idx])
        dfs(idx + 1, a_dist_list, b_dist_list + [b_dist])


    dfs(0, [], [])

    print(f"#{test_case} {min_time}")
