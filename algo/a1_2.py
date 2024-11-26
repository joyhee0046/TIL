## 다리만들기2
# https://www.acmicpc.net/problem/17472


import sys
from collections import deque

# 1. 다리를 생성할 수 있는지 확인하는 함수
def check(li):
    """
    특정 행 또는 열에서 다리를 만들 수 있는 경우를 찾는 함수.
    li: 한 행 또는 한 열을 나타내는 리스트
    """
    start, cnt = 0, 0  # 현재 섬 번호(start)와 다리 길이(cnt)를 초기화
    for idx in range(len(li)):
        if li[idx] > 0:  # 섬을 만난 경우
            if start > 0 and start != li[idx] and cnt >= 2:
                # 다른 섬에 도달했고 다리의 길이가 2 이상인 경우
                edge.append((start, li[idx], cnt))  # 다리 정보를 추가
            start, cnt = li[idx], 0  # 새로운 섬을 시작점으로 설정
        elif start > 0:  # 바다를 만나면 다리 길이 증가
            cnt += 1

# 2. 특정 노드의 부모를 찾는 함수 (Union-Find에서 경로 압축 사용)
def find(v):
    """
    주어진 노드 v의 부모를 찾는 함수.
    경로 압축을 통해 트리의 깊이를 줄임.
    """
    if v != parents[v]:  # 자기 자신이 부모가 아니면 재귀적으로 부모를 찾음
        parents[v] = find(parents[v])  # 부모를 갱신
    return parents[v]

# 3. 두 노드를 하나의 그룹으로 합치는 함수 (Union-Find의 Union 연산)
def union(v1, v2, w):
    """
    두 노드 v1, v2를 하나의 그룹으로 합침.
    두 노드가 같은 그룹에 속하지 않으면 다리를 연결하며 가중치(w)를 더함.
    """
    global answer
    root1, root2 = find(v1), find(v2)  # 두 노드의 루트를 찾음
    if root1 != root2:  # 두 노드가 다른 그룹에 속할 경우
        answer += w  # 최소 다리 길이에 현재 다리 길이를 추가
        # 트리의 높이를 고려하여 병합
        if rank[root1] < rank[root2]:
            parents[root1] = root2  # root1의 부모를 root2로 설정
            rank[root2] += rank[root1]  # root2의 랭크를 갱신
        else:
            parents[root2] = root1  # root2의 부모를 root1으로 설정
            rank[root1] += rank[root2]  # root1의 랭크를 갱신

# 4. 입력 처리
N, M = map(int, input().split())  # 지도 크기: 세로 N, 가로 M
country = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 지도 데이터
cnt = 1  # 섬 번호 (1부터 시작)
queue = deque()  # BFS에서 사용할 큐
edge = []  # 다리 후보 정보를 저장할 리스트

# 5. BFS를 통해 섬에 고유 번호를 붙임
visited = [[False] * M for _ in range(N)]  # 방문 여부를 기록하는 2D 배열
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동 방향

for i in range(N):
    for j in range(M):
        if country[i][j] == 1 and not visited[i][j]:  # 섬이고 아직 방문하지 않았으면
            queue.append((i, j))  # 큐에 추가
            visited[i][j] = True  # 방문 처리
            while queue:  # BFS 실행
                r, c = queue.popleft()
                country[r][c] = cnt  # 현재 섬 번호를 할당
                for dr, dc in direction:  # 상하좌우로 인접한 칸을 탐색
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and country[nr][nc] == 1 and not visited[nr][nc]:
                        queue.append((nr, nc))  # 큐에 추가
                        visited[nr][nc] = True  # 방문 처리
            cnt += 1  # 새로운 섬 번호 증가

# 6. 다리 후보 탐색
for row in country:  # 행 탐색
    check(row)
for col in zip(*country):  # 열 탐색
    check(col)

# 7. 크루스칼 알고리즘 적용
edge = sorted(edge, key=lambda x: x[2])  # 다리 후보를 길이 기준으로 오름차순 정렬
parents = [i for i in range(cnt)]  # 초기 부모는 자기 자신으로 설정
rank = [1] * cnt  # 각 노드의 랭크를 1로 초기화
answer = 0  # 최소 다리 길이 합

for e in edge:  # 정렬된 다리 후보를 하나씩 확인
    union(e[0], e[1], e[2])  # 다리를 연결

# 8. 모든 섬이 연결되었는지 확인
roots = set(find(i) for i in range(1, cnt))  # 각 섬의 루트를 확인
if len(roots) > 1:  # 루트가 여러 개이면 모든 섬이 연결되지 않음
    print(-1)
else:
    print(answer)  # 최소 다리 길이 출력


