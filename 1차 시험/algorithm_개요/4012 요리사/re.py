# import sys
# sys.stdin = open("sample_input.txt", "r")
#
# import itertools
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     synergy = [list(map(int, input().split())) for _ in range(N)]
#
#     food_li = itertools.combinations([i for i in range(N)], N//2)
#
#     for i in food_li:
#         syn_li = itertools.combinations(i, 2)
#         syn_score = synergy[syn_li[0]][syn_li[1]]
#         print(syn_score)
#
#     # itertools로 만들어진 튜플은 그 속성 자체로 저장되어 있기 때문에 len사용이 불가능하다.
#     # list에 담아서 사용할 수 있지만, 복잡해지는 것. 나바보가한건 리스트인덱스를 받아서 리스트 인덱스로 부르기인데,
#     # 그냥 리스트를 차례로 꺼내서 그 자체를 넣으면 되는거였음. ## ..? 안되는데;;
#     # for i in range(len(food_li)):
#     #     syn_li = itertools.combinations(food_li[i], 2)
#     #     syn_score = synergy[syn_li[0]][syn_li[1]]

############################################

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
