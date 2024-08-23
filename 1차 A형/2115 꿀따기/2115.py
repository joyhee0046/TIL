import sys
sys.stdin = open("sample_input.txt", "r")

import itertools
T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    def cal_square_sum(num_list):
        if sum(num_list) > C:
            return 0
        return sum(num ** 2 for num in num_list)

    def cal_max_honey(honey_list):
        max_honey = 0
        for select_cnt in range(1, M+1):
            comb = itertools.combinations(honey_list, select_cnt)
            comb_list = list(map(cal_square_sum, comb))
            max_honey = max(max_honey, max(comb_list))
        return max_honey

    for fst_i in range(N):
        for fst_j in range(N-M+1):
            fst_select_honey_list = matrix[fst_i][fst_j:fst_j+M]
            fst_select_honey_max = cal_max_honey(fst_select_honey_list)
        for snd_i in range(fst_i, N):
            for snd_j in range(0, N-M+1):
                if fst_i == snd_i and snd_j < fst_j + M:
                    continue
                snd_select_honey_list = matrix[snd_i][snd_j:snd_j+M]
                snd_select_honey_max = cal_max_honey(snd_select_honey_list)
                max_sum = max(max_sum, fst_select_honey_max + snd_select_honey_max)
    print(f"#{tc} {max_sum}")