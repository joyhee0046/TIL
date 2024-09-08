import sys
sys.stdin = open('input.txt', 'r')

import itertools, collections

# BFS함수
def bfs(graph, comb, visited, p_sum):
    # 첫번째 요소 큐에 넣고 방문처리
    que = collections.deque([comb[0]])
    visited.add(comb[0])
    # 큐가 빌 때까지
    while que:
        # 요소 하나 빼서 전체 합에 더하기
        node = que.popleft()
        p_sum += p_num[node]
        # 연결되어 있는 노드 하나씩 꺼내기
        for n_node in graph[node]:
            # 이미 방문했던 노드라면 지나가기
            if n_node in visited:
                continue
            # 조합에 안들어있으면, 이번에 방문할 수 없는 요소니까 지나가기
            if n_node not in comb:
                continue
            # 큐에 더하고 방문처리 하기
            que.append(n_node)
            visited.add(n_node)
    # 방문처리된 요소가 확인해야 할 조합 수와 같다면 계산해둔 값 반환
    if len(comb) == len(visited):
        return p_sum
    # 연결되지 않은 점이 있다면 -1 반환
    return -1

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p_num = [0] + list(map(int, input().split()))

    # 조합 만들기
    comb = []
    for i in range(1, N):
        comb.extend(list(itertools.combinations([j for j in range(1,N+1)], i)))

    # 갱신할 큰 값 넣어주기
    min_p = 9999999999

    # 입력을 그래프(딕셔너리)로 넣어주기
    graph = {}
    for i in range(1, N+1):
        x, *y = map(int, input().split())
        graph[i] = y

    # 비교할 전체 노드 리스트 만들기
    total_li = set([j for j in range(1, N + 1)])
    # 만들었던 조합 순회하면서
    for j in comb:
        # 만들어 둔 리스트로 BFS실행
        visited = set()
        p_sum = 0
        ans1 = bfs(graph, j, visited, p_sum)
        # 반환된 값이 -1이라면 해당없으니 지나가기
        if ans1 == -1:
            continue
        # 만든 조합의 역 조합으로 BFS실행
        k = list(total_li - set(j))
        visited = set()
        p1_sum = 0
        ans2 = bfs(graph, k, visited, p1_sum)
        # 반환된 값이 -1이라면 해당없으니 지나가기
        if ans2 == -1:
            continue
        # 차이 계산해서 갱신하기
        min_p = min(min_p, abs(ans1 - ans2))

    # 갱신되지 않았다면_연결되지 않은 노드가 있다면, -1출력
    if min_p == 9999999999:
        min_p = -1
    # 정답 출력
    print(min_p)