import sys
sys.stdin = open('var.txt', 'r')

# # 입력받기
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
# ans = set()
# for i in graph[1]:
#     for j in graph[i]:
#         ans.add(j)
#     # print(ans)
# print(len(ans)-1)


# # 입력받기
# N = int(input())
# M = int(input())
# li = [list(map(int, input().split())) for _ in range(M)]
# cnt = 0
# res = 1
# R_li = [i for i in range(N+1)]
# for a, b in li:
#     if R_li[a] == R_li[b]:
#         continue
#     if (R_li[a] != 1) & (R_li[b] != 1): continue
#     cnt += 1
#     if R_li[a] != res:
#         check = R_li[a]
#         for i in range(N+1):
#             if R_li[i] == check:
#                 R_li[i] = res
#     if R_li[b] != res:
#         check = R_li[b]
#         for i in range(N+1):
#             if R_li[i] == check:
#                 R_li[i] = res
# print(cnt)



class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)  # 부모 노드 배열 초기화
        self.rank = [0] * (len(v) + 1)  # 랭크 배열 초기화
    def make_set(self, x):
        self.p[x] = x  # 각 노드가 자기 자신을 부모로 가지도록 초기화
        self.rank[x] = 0  # 초기 랭크는 0
    def find_set(self, x):
        if x != self.p[x]:  # 노드 x가 자기 자신을 부모로 가지지 않는 경우
            self.p[x] = self.find_set(self.p[x])  # 부모 노드를 재귀적으로 찾고 경로 압축 수행
        return self.p[x]
    def union(self, x, y):
        px = self.find_set(x)  # 노드 x의 대표자(부모) 찾기
        py = self.find_set(y)  # 노드 y의 대표자(부모) 찾기
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py  # x의 부모를 y의 부모로 설정
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px  # y의 부모를 x의 부모로 설정
            else:
                self.p[py] = px  # y의 부모를 x의 부모로 설정
                self.rank[px] += 1  # x의 랭크를 1 증가
V = int(input())
E = int(input())
graph = [list(map(int, input().split())) for _ in range(E)]
idx = list(i for i in range(V+1))
graph.sort(key=lambda x: x[0])

def mst_kruskal(idx, graph):
    mst = []
    n = len(idx)
    ds = DisjointSet(idx)
    for i in range(n + 1):
        ds.make_set(i)
    for edge in graph:
        s, e, w = edge[0], edge[1], 1
        if ds.find_set(s) != ds.find_set(e):
            ds.union(s, e)
            mst.append(edge)
    return ds.p

result = mst_kruskal(idx, graph)
ans = 0
for i in result:
    if i == 1:
        ans += 1

print(ans-1)