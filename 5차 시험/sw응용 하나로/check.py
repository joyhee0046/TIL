import sys
sys.stdin = open("re_sample_input.txt", 'r')

from itertools import combinations

class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)  # 부모 노드 배열 초기화
        self.rank = [0] * (len(v) + 1)  # 랭크 배열 초기화

    def make_set(self, x):
        self.p[x] = x  # 각 노드가 자기 자신을 부모로 가지도록 초기화
        self.rank[x] = 0  # 초기 랭크는 0

    def find_set(self, x):
        if x != self.p[x]:  # 노드 x가 자기 자신을 부모로 가지지 않는 경우
            self.p[x] = self.find_set(self.p[x])
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

def mst_kruskal(vertices, edges):
    mst = []  # 최소 신장 트리 저장
    n = N

    ds = DisjointSet(vertices)

    # 초기화
    for i in range(n + 1):
        ds.make_set(i)

    # 가중치를 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        s, e, w = edge  # 시작정점, 도착정점, 가중치
        if ds.find_set(s) != ds.find_set(e):  # 시작정점과 도착정점이 다른 집합에 속한 경우
            ds.union(s, e)  # 두 집합을 합침
            mst.append(edge)  # 현재 간선을 MST에 추가

    return mst


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mapli = [list(map(int, input().split())) for _ in range(N)]
    E = float(input())
    vertices = list(i for i in range(N + 1))

    island = []
    for i in range(N):
        island.append(mapli[0][i], mapli[1][i]])

    # 섬 연결할 조합 만들기
    island_comb = list(combinations(list(range(1, N + 1)), 2))
    line = []
    # 모든 조합에 대한 비용 계산. 가능한 터널 리스트에 모아두기.
    for comb in island_comb:
        island_1 = island_pos_list[comb[0] - 1]
        island_2 = island_pos_list[comb[1] - 1]
        cost = fee(island_1=island_1, island_2=island_2, e=E)
        line.append((comb[0], comb[1], cost))