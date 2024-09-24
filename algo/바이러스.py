import sys
sys.stdin = open('var.txt', 'r')

# from collections import deque
#
# computer = int(input())
# connect = int(input())
# graph = {}
# for i in range(connect):
#     x, y = map(int, input().split())
#     # 그래프로 만들기.
#     if x not in graph:
#         graph[x] = []
#     graph[x].append(y)
#     if y not in graph:
#         graph[y] = []
#     graph[y].append(x)
# # print(graph)
# # 1이 갈 수 있는 곳
# q = deque([1])
# # 다녀온 곳을 저장
# visited = [1]
#
# cnt = 0
# while q:
#     c_com = q.popleft()
#     for n_com in graph[c_com]:
#         # 이미 다녀온 곳이라면 지나가기
#         if n_com in visited:
#             continue
#         # 아니라면 방문처리하고 큐에 더하기
#         visited.append(n_com)
#         q.append(n_com)
#         # 카운트 올리기
#         cnt += 1
#
# print(cnt)

#########################런타임 에러 (KeyError)###########################

from collections import defaultdict, deque

N = int(input())
M = int(input())

graph = defaultdict(list)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

q = deque([1])
visited = [1]

cnt = 0
while q:
    c_com = q.popleft()

    for n_com in graph[c_com]:
        if n_com in visited:
            continue
        visited.append(n_com)
        q.append(n_com)
        cnt += 1

print(cnt)