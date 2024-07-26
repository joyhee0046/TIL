import sys
sys.stdin = open("sample_input.txt", "r")

# 요리할 수 있는 조합 생성 함수
def comb(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in comb(arr[i + 1:], n - 1):
            result.append([elem] + rest)

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     synergy = [list(map(int, input().split())) for _ in range(N)]
#     point1 = []
#     point2 = []
#     for i in range(0, N):
#         for j in range(i+1, N):
#             point1.append(synergy[i][j] + synergy[j][i])
#             for ii in range(0, N):
#                 if (ii == j or ii == i):
#                     continue
#                 for jj in range(1+ii, N):
#                     if (jj == j or jj == i):
#                         continue
#                     point2.append(synergy[ii][jj] + synergy[jj][ii])
#     diff = []
#     for i in range(len(point1)):
#         diff.append(abs(point1[i]-point2[i]))
#     print(f"#{tc} {min(diff)}")
#




    return result
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    synergy()
    food_list = comb([i for i in range(N)], N/2)

    print(tt_syn)
