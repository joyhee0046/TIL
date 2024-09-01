import sys
sys.stdin = open('re_sample_input.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     xli = list(map(int, input().split()))
#     yli = list(map(int, input().split()))
#     E = int(input())
#
#     lli = [0 for _ in range(N)]
#     tt_l = {}
#     for i in range(N):
#         tt_l[i] = ''
#         for j in range(N):
#             tt_l[i] = (j, ((xli[i] - xli[j])**2 + (yli[i] - yli[j])**2))
#

from itertools import combinations

import heapq


def prim(vertices, edges):
    mst = []  # 최소 신장 트리 저장

    # 인접 리스트 생성
    adj_list = {v: [] for v in vertices}
    for start_v, end_v, w in edges:
        adj_list[start_v].append((end_v, w))
        adj_list[end_v].append((start_v, w))

    visited = set()  # 방문한 노드 집합
    init_vertex = vertices[0]  # 초기 정점
    min_heap = [[w, init_vertex, e] for e, w in adj_list[init_vertex]]  # 초기 정점의 모든 간선을 힙에 추가
    heapq.heapify(min_heap)  # 힙으로 변환
    visited.add(init_vertex)  # 초기 정점 방문

    while min_heap:
        weight, start_v, end_v = heapq.heappop(min_heap)
        if end_v in visited: continue  # 이미 방문한 정점이면 건너뜀

        visited.add(end_v)  # 새로운 정점 방문
        mst.append((start_v, end_v, weight))  # 간선을 MST에 추가

        for adj_v, adj_w in adj_list[end_v]:  # 새로 방문한 정점의 모든 인접 간선 처리
            if adj_v in visited: continue  # 이미 방문한 정점은 건너뜀
            heapq.heappush(min_heap, [adj_w, end_v, adj_v])  # 힙에 간선 추가

    return mst

def cal_env_fee(island_1, island_2, e):
    # 두 섬 사이의 건설비용 계산
    x1, y1 = island_1
    x2, y2 = island_2
    L = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    fee = e * L
    return fee

# 주어진 입력 받기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 섬의 개수
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())

    # 섬 위치 좌표로 만들어주기
    island_pos_list = []
    for x, y in zip(x_list, y_list):
        island_pos_list.append((x, y))

    # 섬 연결할 조합 만들
    island_comb = list(combinations(list(range(1, N + 1)), 2))
    tunnels = []
    # 모든 조합에 대한 비용 계산. 가능한 터널 리스트에 모아두기.
    for comb in island_comb:
        island_1 = island_pos_list[comb[0] - 1]
        island_2 = island_pos_list[comb[1] - 1]
        env_fee = cal_env_fee(island_1=island_1, island_2=island_2, e=E)
        tunnels.append((comb[0], comb[1], env_fee))

    # 결과. 메인함수 실행하기
    cost = round(kruskal_mst(vertices=list(range(1, N + 1)), edges=tunnels))
    # 정답 출력하기
    print(f"#{tc} {cost}")