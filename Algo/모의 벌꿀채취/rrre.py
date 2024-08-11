import sys
sys.stdin = open("sample_input1.txt", 'r')

import itertools
# 주어진 입력 받기
T = int(input())
for tc in range(1, 1+T):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    # 모은 꿀 확인할 배열
    honey_check = [[0] * N for _ in range(N)]

    # 채취할 수 있는 꿀 확인하기
    for row in range(N):
        for col in range(N-M+1):
            picks = []
            ans = []
            for pick in range(M):
                ans.append(honey[row][col+pick])
                picks.append(honey[row][col + pick] ** 2)

            # 고른 꿀이 딸 수 있는 꿀보다 많다면
            if sum(ans) > C:
                for subtract in range(1, M):
                    cnt = 0
                    # 조합 확인해서 꿀을 가장 많이 채취
                    honey_volume = list(itertools.combinations(picks, M - subtract))
                    for honey_way in itertools.combinations(ans, M-subtract):
                        if sum(honey_way) > C:
                            cnt += 1
                            continue
                        honey_check[row][col] = max(sum(honey_volume[cnt]), honey_check[row][col])
                        cnt += 1

                continue
            # 고른 꿀을 다 딴다면
            honey_check[row][col] = sum(picks)

    # 체크리스트에서 가장 큰 수 두 개, 근데 옆자리가 아닌.
    fst_max = [1,[[9,9]for _ in range(M)]]
    snd_max = [1,[[9,9]for _ in range(M)]]
    # for i in range(N):
    #     for j in range(N):
    #         if honey_check[i][j-1] != fst_max and fst_max < honey_check[i][j]:
    #             snd_max = fst_max
    #             fst_max = honey_check[i][j]
    #
    #         elif honey_check[i][j-1] != fst_max and snd_max < honey_check[i][j]:
    #             snd_max = honey_check[i][j]
    #

    # 가장 많은 꿀통 고르기
    for i in range(N):
        for j in range(N):
            ### 범위로. M범위,, 3개씩 선택하면 앞에 3칸 남겨줘야 하니까ㅣ. 지금은 2개 선택하는 상황에서랄까.
            # for subtract in range(1, M):78
            #
            #             if fst_max[0] < honey_check[i][j]:
            #                 fst_max = [honey_check[i][j], [i, j]]

                if fst_max[0] < honey_check[i][j]:
                    if honey_check[i][j - subtract] == fst_max[0]:
                        if fst_max[1] == [i, j - subtract]:
                            continue
                    snd_max = fst_max
                    fst_max = [honey_check[i][j], [i, j]]

                elif snd_max[0] < honey_check[i][j]:
                    snd_max = [honey_check[i][j], [i, j]]

    print(f"#{tc} {fst_max[0]+snd_max[0]}")