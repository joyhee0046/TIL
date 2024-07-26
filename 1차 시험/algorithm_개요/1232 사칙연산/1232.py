# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# for tc in range(10) :
#     N = int(input())
#     Vt_info = [list(map(input().split()))for _ in range(N)]
#     subtree = []
#     point1 = 0
#     point2 = 0
#     for i in range(N) :
#         if Vt_info[i][0] in  ['+', '-', '*', '/'] :
#             subtree.append(Vt_info[i][0])
#             if Vt_info[i][0] == point1 :
#                 ##연산자가 있으면 뒤에 따라오는
#             point1 = Vt_info[i][1]
#             point2 = Vt_info[i][2]


import sys
sys.stdin = open("input.txt", "r")

# #리스트로 풀기
#
def in_order(node) :
    if node:
        in_order(data[node][1]) #left
        return exp.append(in_order(data[node][3]))
        in_order(data[node][2]) #right


for tc in range(1,11):
    N = int(input())
    data = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    # 람다 안쓰고 입력받기
    # data = [list(input().split()) for _ in range(N)]
    # for i in range(N):
    #     for j in range(len(data[i])):
    #         if data[i][j].isdecimal():
    #             data[i][j] = int(data[i][j])
    for arr in data :
        while len(arr) != 4:   #입력길이를 맞추려고
            arr.append(0)

    exp=[]

    data.insert(0, [0,0,0,0])



    print(f"#{tc}", end=' ')
    in_order(1)
    print(exp)