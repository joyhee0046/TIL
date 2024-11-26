## 보석 도둑
# 도둑은 가장 가까운 보석으로 항상 이동하며 자신 기준으로 보석이 같은 거리에 있을 경우 폭탄이 터짐. 폭탄이 터지지 않으면서 가장 적게 이동할 수 있는 시작 위치를 찾고 거리를 구해라.

def checker(start_point, def_jewels):
    current_pos = start_point

    while def_jewels:
        # 현재 위치 기준 가장 가까운 왼쪽, 오른쪽 보석 찾기
        left = [j for j in def_jewels if j < current_pos]
        right = [j for j in def_jewels if j > current_pos]

        # 가장 가까운 왼쪽/오른쪽 보석 거리 계산
        left_dist = current_pos - left[-1] if left else float('inf')
        right_dist = right[0] - current_pos if right else float('inf')

        # 폭발 조건 확인
        if left_dist == right_dist:  return False  # 폭발 발생

        # 가까운 보석으로 이동
        if left_dist < right_dist:  next_pos = left[-1]
        else:                       next_pos = right[0]

        # 보석 먹기
        def_jewels.remove(next_pos)
        current_pos = next_pos

    return True  # 모든 보석을 성공적으로 먹음

n, k = map(int, input().split())  # 보석 개수 / 출발 idx
maps = list(map(int, input().split()))
jewels = []
for i in range(len(maps)):
    if maps[i] == 1:
        jewels.append(i)

# k : idx >> 0 번째 가능

flag = False

if checker(k, jewels[:]):
    print(0)

else:
    r = 1
    while 1:
        fail_flag = 0
        for dx in [r, -r]:  # 0일때 에러나나 ? 동일한 요소로 2번 도니까 ?
            nx = k + dx   # k에서 이동한 시작 위치
            if nx < 0 or nx >= len(maps):  # 범위 밖이면 이쪽으로는 그만 뻗어야  # 둘다 범위 밖이면 -1 출력
                fail_flag += 1
                continue

            elif maps[nx] == 1: continue  # 보석 있으면 출발 못함

            else:  # 범위 안이고 보석 찾으러 출발 가능
                flag = checker(nx, jewels[:])  # 시작 좌표 : nx

            if flag:break  # 답 나옴 > 다음 요소 볼 필요 없음

        if flag:
            print(r)
            break

        if fail_flag == 2:  # 왼오 다 갈곳 없음 > k 다 뻗었는데 성공을 못함
            print(-1)
            break

        r += 1


