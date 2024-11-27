## 보석 도둑
# 도둑이 직선상에 위치
# 도둑은 가장 가까운 보석으로 항상 이동하며 자신 기준으로 보석이 같은 거리에 있을 경우 폭탄이 터짐.
# 폭탄이 터지지 않으면서 가장 적게 이동할 수 있는 시작 위치를 찾고 거리를 구해라.

def checker(start_point, def_jewels):
    """
    주어진 시작 위치에서 폭발 없이 모든 보석을 먹을 수 있는지 확인하는 함수.

    Args:
        start_point (int): 도둑의 시작 위치 (인덱스).
        def_jewels (list): 보석 위치가 저장된 인덱스 리스트.

    Returns:
        bool: 모든 보석을 먹을 수 있으면 True, 폭발이 발생하면 False.
    """
    current_pos = start_point  # 도둑의 현재 위치.

    while def_jewels:  # 보석이 남아 있는 동안 반복.
        # 현재 위치 기준으로 왼쪽과 오른쪽 보석을 찾음.
        left = [j for j in def_jewels if j < current_pos]  # 현재 위치보다 왼쪽에 있는 보석.
        right = [j for j in def_jewels if j > current_pos]  # 현재 위치보다 오른쪽에 있는 보석.

        # 가장 가까운 보석까지의 거리 계산.
        left_dist = current_pos - left[-1] if left else float('inf')  # 왼쪽에서 가장 가까운 보석 거리.
        right_dist = right[0] - current_pos if right else float('inf')  # 오른쪽에서 가장 가까운 보석 거리.

        # 폭발 조건: 왼쪽과 오른쪽 보석이 같은 거리에 있는 경우.
        if left_dist == right_dist:
            return False  # 폭발 발생 (실패 처리).

        # 더 가까운 보석으로 이동.
        if left_dist < right_dist:
            next_pos = left[-1]  # 왼쪽의 가장 가까운 보석으로 이동.
        else:
            next_pos = right[0]  # 오른쪽의 가장 가까운 보석으로 이동.

        # 이동한 보석을 먹음 (리스트에서 제거).
        def_jewels.remove(next_pos)
        current_pos = next_pos  # 현재 위치를 새로 먹은 보석의 위치로 갱신.

    return True  # 모든 보석을 먹었으면 성공 처리.


# 입력 처리.
n, k = map(int, input().split())  # n: 전체 맵 크기, k: 도둑의 시작 위치 인덱스.
maps = list(map(int, input().split()))  # 맵의 상태 (0: 빈 칸, 1: 보석).
jewels = []  # 보석의 위치를 저장할 리스트.
for i in range(len(maps)):
    if maps[i] == 1:
        jewels.append(i)  # 보석이 있는 위치를 리스트에 추가.

# k : idx >> 0 번째 가능
flag = False

# 초기 위치에서 바로 가능한지 검사.
if checker(k, jewels[:]):  # 현재 위치(k)에서 폭발 없이 모든 보석을 먹을 수 있다면.
    print(0)  # 이동 거리 0 출력 (추가 이동 필요 없음).

else:  # 다른 시작 위치를 탐색.
    r = 1  # 탐색 거리 초기화.
    while True:
        fail_flag = 0  # 왼쪽(-r)과 오른쪽(+r)의 실패 횟수를 기록.
        for dx in [r, -r]:  # 오른쪽(+r)과 왼쪽(-r)을 각각 탐색.
            nx = k + dx  # 새로운 시작 위치 계산.

            # 새로운 위치가 유효한지 확인.
            if nx < 0 or nx >= len(maps):  # 맵 범위를 벗어난 경우.
                fail_flag += 1  # 실패로 간주.
                continue

            elif maps[nx] == 1:  # 보석 위치인 경우.
                continue  # 보석 위에서는 시작할 수 없으므로 건너뜀.

            else:  # 빈 칸(0)인 경우.
                flag = checker(nx, jewels[:])  # 새로운 시작 위치(nx)에서 가능한지 확인.

            if flag:  # 가능한 위치를 찾은 경우.
                break  # 더 이상 탐색할 필요 없음.

        if flag:  # 성공적으로 시작 위치를 찾은 경우.
            print(r)  # 필요한 최소 이동 거리 출력.
            break

        if fail_flag == 2:  # 왼쪽(-r)과 오른쪽(+r) 모두 실패한 경우.
            print(-1)  # 가능한 시작 위치가 없음을 나타냄.
            break

        r += 1  # 탐색 거리를 증가.
