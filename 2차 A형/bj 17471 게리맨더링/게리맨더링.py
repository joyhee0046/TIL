import sys
sys.stdin = open('input.txt', 'r')

import itertools, collections

def bfs(graph, comb, visited, p_sum):
    que = collections.deque([comb[0]])
    while que:
        # print(que)
        node = que.popleft()
        p_sum += p_num[node]
        for n_node in graph[node]:
            if n_node in visited:
                continue
            que.append(n_node)
            visited.add(n_node)
    if len(comb) == len(visited):
        return p_sum
    return -1

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p_num = [0] + list(map(int, input().split()))

    visited = set()

    comb = []
    for i in range(1, N):
        comb.extend(list(itertools.combinations([j for j in range(1,N+1)], i)))
    # print(comb)

    min_p = 9999999999

    graph = {}
    for i in range(1, N+1):
        x, *y = map(int, input().split())
        graph[i] = y
    # print(graph)

    for j in comb:
        # print(j)
        p_sum = 0
        min_p = min(min_p, bfs(graph, j, visited, p_sum))

    print(min_p)
