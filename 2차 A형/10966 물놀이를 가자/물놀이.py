## 20 中 5 통과 후 제한시간 초과
import sys
sys.stdin = open('sample_input.txt', 'r')

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    summer_map = [list(input()) for _ in range(N)]

    water_spot = []
    land_spot = []
    # 모든 칸 확인하기, 땅이 어디고 물이 어딘지
    for i in range(N):
        for j in range(M):
            if summer_map[i][j] == 'W':
                water_spot.append((i, j))
                continue
            land_spot.append((i, j))

    ans = 0
    # 물까지 이동하는 길 구하기
    for a in land_spot:
        dist = []
        for b in water_spot:
            # a부터 b까지 거리구하기
            ax, ay = a[0], a[1]
            bx, by = b[0], b[1]
            cal_dist = abs(ax - bx) + abs(ay - by)
            dist.append(cal_dist)
        ans += min(dist)

    print(f"#{tc} {ans}")