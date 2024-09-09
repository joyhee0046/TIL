### 점심 식사시간_DFS_1계단 2계단 중 선택하여 가장 합리적인 선택하기
import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque

# 자리부터 계단까지 거리 구하기
def get_dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 계단 내려가는 중_계단 내 최대인원 3명_문제조건
def down_stairs(stair_on_list):
    for idx in range(3):
        # 내려가는 중이면 1씩 줄여주기. 0이 되면 끝
        if stair_on_list[idx] != 0:
            stair_on_list[idx] -= 1
    return stair_on_list

# 계단 진입시키기 함수
def place_people_on_stairs(waiting_queue, stair_on_list, stair_len, cnt_time):
    for stair_idx in range(3):
        # 계단을 내려가야하는 사람이 남았고, 시간이 충분히 흘러서 이미 도착했으며, 계단에 빈 자리가 있다면
        if waiting_queue and waiting_queue[0] <= cnt_time and stair_on_list[stair_idx] == 0:
            # 기다리는 사람 꺼내서 출발시키기
            pop_data = waiting_queue.popleft()
            if pop_data == cnt_time:
                # 방금 막 도착했다면 1초 기다리고 출발_문제조건
                stair_on_list[stair_idx] = stair_len + 1
            else:
                stair_on_list[stair_idx] = stair_len
    return

# 메인 함수
def dfs(idx, a_dist_list, b_dist_list):
    global min_time
    # 현재까지 최소 거리보다, 가장 늦게 도착한 사람 + 계단 길이인 경우에는 아래 로직을 계산하지 않음_가지치기
    if a_dist_list and min_time <= max(a_dist_list) + stair_list[0][2]:
        return
    if b_dist_list and min_time <= max(b_dist_list) + stair_list[1][2]:
        return
    # 모든 사람에 대해 확인했다면,
    if idx == len(people_list):
        # queue 구현해서 최종 시간에 따라 최소시간 갱신하기
        t = 0
        a_stair_on_list = [0] * 3
        b_stair_on_list = [0] * 3

        # 이미 계단 배정이 완료되었으니, 정렬_누구부터 내보낼지
        a_dist_list.sort()
        b_dist_list.sort()
        # 계단별로 큐 만들기
        a_queue = deque(a_dist_list)
        b_queue = deque(b_dist_list)

        # 사람이 남아있다면 계속 돌기
        while True:
            if sum(a_stair_on_list) > 0:
                # 계단 내려가기 함수
                a_stair_on_list = down_stairs(a_stair_on_list)
            if sum(b_stair_on_list) > 0:
                b_stair_on_list = down_stairs(b_stair_on_list)
            if a_dist_list and a_dist_list[0] <= t:
                # 계단 진입시키기 함수
                place_people_on_stairs(a_queue, a_stair_on_list, stair_list[0][2], t)
            if b_dist_list and b_dist_list[0] <= t:
                place_people_on_stairs(b_queue, b_stair_on_list, stair_list[1][2], t)
            # 첫둘 계단을 내려가는 중인 사람 없고, 첫둘계단을 기다리는 중인 사람이 없다면 끝
            if not a_queue and not b_queue and sum(a_stair_on_list) == 0 and sum(b_stair_on_list) == 0:
                break
            # 시간 +1
            t += 1
            if min_time <= t:
                return
        # 최소시간 갱신
        min_time = min(min_time, t)
        return
    # 선택한 사람을 첫번째 계단으로 보내기
    a_dist = get_dis(stair_list[0][:2], people_list[idx])
    dfs(idx + 1, a_dist_list + [a_dist], b_dist_list)
    # 선택한 사람을 두번째 계단으로 보내기ㅛ
    b_dist = get_dis(stair_list[1][:2], people_list[idx])
    dfs(idx + 1, a_dist_list, b_dist_list + [b_dist])

# 주어진 입력 받기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    min_time = 999999

    # 사람 위치와 계단 위치 확인해주기
    people_list = []
    stair_list = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0:
                continue
            elif maps[i][j] == 1:
                people_list.append([i, j])  # 사람 좌표
            else:
                stair_list.append([i, j, maps[i][j]])  # 계단 좌표와 내려가는 시간
    # 메인 함수 실행
    dfs(0, [], [])
    # 출력하기
    print(f"#{tc} {min_time}")