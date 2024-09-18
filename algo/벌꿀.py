import sys
sys.stdin = open('1_sample_input.txt', 'r')

from itertools import combinations

# 메인 함수
def calculate_profit(honey):
    # 최대 수익을 담을 변수. 갱신을 위해 최소로 설정
    max_profit = 0
    # m번 돌면서
    for i in range(1, len(honey) + 1):
        for comb in combinations(honey, i):
            # 채취할 꿀이 최대량 이하라면
            if sum(comb) <= c:
                # 최대 수익 계산하고 갱신
                max_profit = max(max_profit, sum([x ** 2 for x in comb]))
    # 최대 수익
    return max_profit

# 주어진 입력받기
T = int(input())
for tc in range(1, T + 1):
    # n = 벌통크기, m = 선택가능수, c = 최대꿀량
    n, m, c = list(map(int, input().split()))
    # 벌집지도
    maps = [list(map(int, input().split())) for _ in range(n)]

    # 각 줄에서 선택 가능한 벌통의 최대 수익 계산
    profits = []
    for i in range(n):
        # 선택할 벌통의 범위 설정
        for j in range(n - m + 1):
            # m개의 벌통 선택
            honey = maps[i][j:j + m]
            # 선택한 벌통에 대하여 메인 함수 시작
            profit = calculate_profit(honey)
            # 수익과 위치 저장
            profits.append((profit, (i, j, j + m - 1)))

    # 정답 갱신할 변수
    max_total_profit = 0
    # 두 벌통이 겹치지 않도록 조합을 선택
    for (profit1, (x1, y1_start, y1_end)), (profit2, (x2, y2_start, y2_end)) in combinations(profits, 2):
        # 다른 줄에 있거나, 같은 줄이라도 겹치지 않을 때
        if x1 != x2 or y1_end < y2_start:
            # 딸 수 있는 최대 이익 갱신
            max_total_profit = max(max_total_profit, profit1 + profit2)
    # 정답 출력
    print(f'#{tc} {max_total_profit}')