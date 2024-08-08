import sys
sys.stdin = open("sample_input.txt", 'r')

# 주어진 입력 받기
T = int(input())
for tc in range(1, 1+T):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    honey_check = [[0]*N for _ in range(N)]

    revenue = 0
    fst_honey = 0
    snd_honey = 0
    for row in range(N):
        for col in range(N-M+1):
            picks = []
            ans = 0
            for pick in range(M):
                ans += honey[row][col+pick]
                xy.append([row, col + pick])
                picks.append(honey[row][col + pick] ** 2)
            if ans > C:
                if fst_honey < max(picks):
                    snd_honey = fst_honey
                    fst_honey = max(picks)

                elif snd_honey < max(picks):
                    snd_honey = max(picks)


                continue
            if fst_honey < sum(picks):
                snd_honey = fst_honey
                fst_honey = sum(picks)

            elif snd_honey < sum(picks):
                snd_honey = sum(picks)

        revenue = fst_honey + snd_honey


    print(revenue)