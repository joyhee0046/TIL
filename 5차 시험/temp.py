## 서로소 집합
N = 10
p = [0] * (N + 1)  # 부모 노드 리스트 초기화
rank = [0] * (N + 1)  # 랭크 리스트 초기화
def make_set(x):
    p[x] = x  # 각 노드가 자기 자신을 부모로 가지도록 초기화
"""
# 최적화 전 find_set
def find_set(x):
    if x == p[x]:  # 노드 x가 자기 자신을 부모 노드로 가지는 경우 그대로 반환 
        return x
    return find_set(p[x])  # 부모 노드를 재귀적으로 찾고 반환
"""
# 경로 압축을 적용한 find_set
def find_set(x):
    if x != p[x]:  # 노드 x가 자기 자신을 부모로 가지지 않는 경우
        p[x] = find_set(p[x])  # 부모 노드를 재귀적으로 찾고 경로 압축 수행
    return p[x]
"""
# 최적화 전 union 함수
def union(x, y):
    px = find_set(x)  # 노드 x의 대표자(부모) 찾기
    py = find_set(y)  # 노드 y의 대표자(부모) 찾기

    if px < py:  # 값이 더 작은 부모가 큰 부모에게 union
        p[py] = px
    else:
        p[px] = py
"""
# 랭크를 이용한 union 함수
def union(x, y):
    px = find_set(x)  # 노드 x의 대표자(부모) 찾기
    py = find_set(y)  # 노드 y의 대표자(부모) 찾기

    if px != py:  # 두 노드가 서로 다른 집합에 속해 있는 경우에만 합침
        if rank[px] > rank[py]:  # 랭크가 높은 트리에 붙임
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px  # 랭크가 같은 경우 하나를 다른 하나의 부모로 설정
            rank[px] += 1  # 랭크 증가
# 초기화 예시
for i in range(1, N + 1):
    make_set(i)
# union 연산 예시
union(1, 2)
union(2, 3)
print(find_set(1))  # 출력: 1
print(find_set(2))  # 출력: 1


## 서로소 집합_그룹나누기
# 올바른 대표자 찾기
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]
# 그룹 연결시키기
def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if px != py:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1

T = int(input())
for tc in range(1, 1 + T):
		# N번까지의 출석번호가 있고, M장의 팀 신청서
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    p = [i for i in range(0, 1 + N)]  # 부모 노드 리스트 초기화
    rank = [0] * (N + 1)  # 랭크 리스트 초기화
    for i in range(0, len(li), 2):
        union(li[i], li[i+1])
    # 연결할 자리를 찾아준 후에, 잎을 루트로 연결해주는 동작.
    for i in range(1, N+1):
        p[i] = find_set(i)
    print(f'#{tc} {len(set(p))-1}')


## 서로소 집합_ 최소 신장 트리
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

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    vertices = list(i for i in range(V+1))
    #크로스칼 알고리즘 사용
    def mst_kruskal(vertices, edges):
        mst = []  # 최소 신장 트리 저장
        n = V+1  # 0번부터 V번까지라서
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
    result = mst_kruskal(vertices, edges)
    ans = 0
    for i in range(len(result)):
        ans += result[i][2]
    print(f"#{tc} {ans}")


## 서로소 집합_하나로
from itertools import combinations
class DisjointSet:
    def __init__(self, number_of_items):
        self.head = [0 for _ in range(number_of_items + 1)]   # 부모 노드 배열 초기화
        self.rank = [0 for _ in range(number_of_items + 1)]   # 랭크 배열 초기화
        self.n = number_of_items
    def make_set(self, item):
        self.head[item] = item   # 각 노드가 자기 자신을 부모로 가지도록 초기화
        #없어도되는?# self.rank[item] = 0  # 초기 랭크는 0
    # 메인함수에서 for문 돌리지 않고 초기화 과정을 함수로 정의.
    def make_set_all(self):
        for item in range(1, self.n + 1):
            self.make_set(item)
    def find_head(self, item):
        if self.head[item] != item:  # 노드 item가 자기 자신을 부모로 가지지 않는 경우
            self.head[item] = self.find_head(self.head[item])  # 부모 노드를 재귀적으로 찾고 경로 압축 수행
        return self.head[item]
    def find_head_all(self):
        n = len(self.head)
        for item in range(1, n + 1):
            self.find_head(item)
    def union(self, item1, item2):
        h1 = self.find_head(item1)  # item1의 대표자 찾기
        h2 = self.find_head(item2)  # item2의 대표자 찾기
        if h1 != h2:
            if self.rank[h1] > self.rank[h2]:
                self.head[h2] = h1   # 2의 부모를 1로 설정
            elif self.rank[h1] < self.rank[h2]:
                self.head[h1] = h2   # 1의 부모를 2로 설정
            else:
                self.head[h2] = h1    # 2의 부모를 1로 설정
                self.rank[h1] += 1   # 1의 랭크 1 증가

def kruskal_mst(vertices, edges):
    n = len(vertices)
    edges.sort(key=lambda x: x[2])  # 환경 부담금 기준 정렬 (오름차순)
    ds = DisjointSet(n)
    ds.make_set_all()
    mst_cost = 0
    mst_edges = 0
    mst_edge_list = []
    for edge in edges:
        v, u, w = edge
        if ds.find_head(v) != ds.find_head(u):  # 시작정점과 도착정점이 다른 집합에 속한 경우
            ds.union(v, u)   # 두 집합을 합침
            # 현재 간선을 MST에 추가
            mst_edges += 1
            mst_cost += w
            mst_edge_list.append(edge)
    return mst_cost

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
    # 섬 연결할 조합 만들기
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


## DP_타일붙이기
def fibo_dp(n):
    if n <= 3: return n  # 모형이 3단위까지 있음. 이후로는 조합
    dp = [0] * (n + 1)
    dp[1] = 1   # 1이 가질 수 있는 경우의 수 1
    dp[2] = 3   # 2의 경우의 수 3
    dp[3] = 6   # 3 경우의 수 6
    for i in range(4, n + 1):  # 점화식 세우고 목표까지 계산
        dp[i] = dp[i-1] + (dp[i-2] * 2) + dp[i-3]
    return dp[n]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {fibo_dp(N)}')


## DP_이항계수
def bino(n, k):
	# 배열 초기화
	B = [[0 for _ in range(k+1)] for _ in range(n+1)]
	# dp테이블 채우기
	for i in range(n+1):
		for j in range(min(i,k)+1):
			# 기본 케이스
			if j==0 or j==i:
				B[i][j] = 1
			else:
				# 이항계수 계산
				B[i][j] = B[i-1][j-1] + B[i-1][j]
	# nCk값 반환
	return B[n][k]

T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    print(f"#{tc} {bino(n, b)}")


## DP_해피박스
# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(M)]
    # 2차원 배열 만들기
    dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    # 1부터 시작하는 이유 :
    # i(아무 가방도 없는 경우)가 0인 경우 모두 0, j(최대 담을 수 있는 사이즈가 0인 경우)가 0인 경우도 모두 0의 값을 가진다.
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            # 담을 물건의 크기가 현재 담을 수 있는 크기보다 큰 경우
            if li[i - 1][0] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - li[i - 1][0]] + li[i - 1][1], dp[i - 1][j])
    result = dp[-1][-1]
    print(f'#{tc} {result}')


## 최단경로 기본_정렬된 부분 집합
def find_ans(nums):
    dp = [1] * n
		# 모든 쌍 비교
    for i in range(n):
        for j in range(i):
						# 나보다 다음이 큰지 확인_문제조건이 오름차순
            if nums[j] < nums[i]:
								# 몇 번째 원소를 확인한건지, 저장_문제조건이 가장 많은 원소를 가지는 부분집합
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
# 주어진 입력
T = int(input())
for tc in range(1, T+1):
    li = list(map(int, input().split()))
    n = li[0]
    nums = li[1:]
		# 정답 출력
    print(f"#{tc} {find_ans(nums)}")


## 최단경로 기본_그래프 최소 비용
T = int(input())
INF = float('inf')
for tc in range(1, T + 1):
    N = int(input())
    adj_matrix = [list(map(int, input().split())) for _ in range(N)]
    # 인접 행렬 초기화
    # r != c 이면서 a_ij 가 0인 경우 즉, 인접하지 않은 경우 INF 할당
    for r in range(N):
        for c in range(N):
            if r == c: continue
            if adj_matrix[r][c] == 0:
                adj_matrix[r][c] = INF
    # 모든 정점을 경유 정점(k)으로 지정
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if adj_matrix[i][j] > adj_matrix[i][k] + adj_matrix[k][j]:
                    adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
    # 최단 경로 중 가장 큰 값
    max_shortest = 0
    for r in range(N):
        for c in range(N):
            if max_shortest < adj_matrix[r][c]:
                max_shortest = adj_matrix[r][c]
    print(f"#{tc} {max_shortest}")


## 최단경로 Dijkstra_최소 이동 거리
import heapq
T = int(input())
INF = float('inf')
for tc in range(1, T + 1):
    N, E = map(int, input().split())  # N: 연결 지점 번호, E: 도로의 개수
    adj_matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    # print(adj_matrix)
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_matrix[s][e] = w
    # vertex 0에서 각 vertex로의 거리를 저장할 리스트
    distances = [INF for _ in range(N + 1)]
    # 시작 정점의 거리는 0으로 설정
    distances[0] = 0
    # 시작 정점과 거리를 우선순위 큐에 삽입
    heap = []  # (w_i, v_i)
    heapq.heapify(heap)
    heapq.heappush(heap, (0, 0))
    while heap:
        # 가장 짧은 거리를 가지는 정점 추출
        w, v = heapq.heappop(heap)
        if distances[v] < w: continue
        # 추출한 정점과 인접한 정점을 모두 확인
        for u, connected in enumerate(adj_matrix[v]):
            # print(adj_matrix[v])
            if not connected: continue
            if distances[u] > distances[v] + adj_matrix[v][u]:
                distances[u] = distances[v] + adj_matrix[v][u]
                heapq.heappush(heap, (distances[u], u))
    print(f"#{tc} {distances[-1]}")


################################################
## 파핑 지뢰찾기
import sys

sys.stdin = open("input.txt", "r")

from collections import deque

dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    borad = [list(input()) for _ in range(N)]
    ans = 0
    borad_check = [[False] * N for _ in range(N)]

    # 전체 탐색
    for i in range(N):
        for j in range(N):
            # 지뢰 먼저 찾아서 방문처리. 탐색 중에 지뢰를 누르지 못하게
            if borad[i][j] == '*':
                borad_check[i][j] = True
                continue
            # 선택된 자리를 기준으로 8방에 지뢰가 있는지 확인해주기
            # 선택+8방해서 9곳에 지뢰가 없다면 재귀하기 위해서 주변에 지뢰 여부 확인.
            boom_cnt = 0
            for dx, dy in dxy:
                ni, nj = i + dx, j + dy
                # 보드판을 벗어나면 넘어가기
                if 0 > ni or ni >= N or 0 > nj or nj >= N: continue
                # 지뢰면 카운트 올리기
                if borad[ni][nj] == '*':
                    boom_cnt += 1
            # 보드판을 수정해서 탐색 과정에서 확인할 수 있도록
            borad[i][j] = boom_cnt

    # 완탐할건데, 9자리에 폭탄 없으면 재귀_큐에 넣어서
    for i in range(N):
        for j in range(N):
            # 주변에 폭탄이 있으면 넘어가기
            if borad[i][j] != 0: continue
            # 전에 확인한 자리_이거나 폭탄_면 넘어가기
            if borad_check[i][j]: continue
            # 확인해야 하는 자리 큐에 넣고
            queue = deque([(i, j)])
            # 방문처리
            borad_check[i][j] = True
            # 큐가 비어있지 않다면 계속 실행
            while queue:
                # 확인할 좌표 뽑아주고
                ci, cj = queue.popleft()
                # 주변에 폭탄이 있다면 넘어가기
                if borad[ci][cj] != 0: continue
                # 8방 탐색
                for dx, dy in dxy:
                    ni, nj = ci + dx, cj + dy
                    # 보드판 범위를 벗어난다면 넘어가기
                    if 0 > ni or ni >= N or 0 > nj or nj >= N: continue
                    # 폭탄이면 넘어가기
                    if borad[ni][nj] == '*': continue
                    # 방문했던 곳이면 넘어가기
                    if borad_check[ni][nj]: continue
                    # 맨땅이라면 방문체크하고 큐에 넣기_한 덩어리로 터질 수 있는 옆칸 확인용 재귀
                    borad_check[ni][nj] = True
                    queue.append((ni, nj))
            # 정답 카운트 하나 올리기
            ans += 1

    # 방문처리 되지 않은 칸 하나씩 눌러주기
    for i in range(N):
        for j in range(N):
            if not borad_check[i][j]:
                ans += 1

    # 정답 출력
    print(f"#{test_case} {ans}")

##################################
## 디저트카페
import sys
sys.stdin = open("sample_input.txt", "r")


def dfs(cx, cy, mv_dir, visited_desert):
    global max_shop_cnt

    # 시작 지점(si, sj) = 현재 지점(cx, cy) 과 같고, 방향이 3  => 최고 방문 가게 수를 갱신
    if [s_i, s_j] == [cx, cy] and mv_dir == 3:
        max_shop_cnt = max(max_shop_cnt, len(visited_desert))
        return

    # 내가 가게의 절반을 돌았는데, 현재까지 저장된 최대 디저트 개수의 절반도 못먹었다? 가지치기
    if mv_dir == 2 and max_shop_cnt >= len(visited_desert) * 2:
        return

    # 좌표 범위를 벗어났는 지 확인
    if cx < 0 or cx >= N or cy < 0 or cy >= N: return

    # 지금 방문한 가게의 디저트를 섭취한 경우
    if arr[cx][cy] in visited_desert: return

    # 현재 위치 방문 처리
    visited_desert.add(arr[cx][cy])

    # 현재 방향에 따라서 이동한다.
    nx, ny = cx + dxy[mv_dir][0], cy + dxy[mv_dir][1]

    dfs(nx, ny, mv_dir, visited_desert)  # 현재 방향을 유지한 채로 보내고

    if mv_dir < 3:  # 오른쪽 윗 대각선이 아니라면, 방향을 꺾어서 진행한다.
        dfs(nx, ny, mv_dir + 1, visited_desert)  # 현재 방향에서 꺾은 채로 보낸다.

    # 현재 위치의 방문 처리를 취소해야한다.
    visited_desert.remove(arr[cx][cy])

# 0: 오른쪽 대각선 아래, 1: 왼쪽 아래 대각선, 2: 왼쪽 위 대각선, 3: 오른쪽 위 대각선
dxy = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_shop_cnt = -1

    for s_i in range(N - 2):  # 행을 나타내고, 마지막 2개의 행은 돌지 않는다._마름모로 돌아야 해서_문제조건
        for s_j in range(1, N - 1):  # 열은 나타내고, 첫 번째 열은 돌지 않는다._마름모로 돌아야 해서_문제조건
            dfs(s_i, s_j, 0, set())  # 시작좌표, 방향, 먹은 디저트

    print(f"#{tc} {max_shop_cnt}")

##################################################
## 보호필름
def inspect():
    for w in range(W):
        k_sum = 1
        for j in range(D - 1):
            # 다음 셀이랑 비교해서 일치하면 +1, 다르면 초기화
            if matrix[j][w] == matrix[j + 1][w]:
                k_sum += 1
            else:
                k_sum = 1
            # 기준치를 만족시키면 중단
            if k_sum == K:
                break
        else:  # for 문이 끝까지 돌았다는 건 없다는 것
            return False
    return True

# remain_cnt : 남은 투입 횟수
# start_idx : 다음 투입을 어디서부터 시작할건지
def dfs(remain_cnt, start_idx):
    # 남은 투입횟수가 0 이되면 검사
    # 투입횟수 횟수로 바꿔도 됩니다.
    if remain_cnt == 0:
        return inspect()

    """
    현재 집어넣은 위치 이전에는 제외하고 투입을 한다. 
    그 다음부터 투입을 하면 된다. 
    dfs 가 진행될 수록 투입 시작 위치는 +1 이 되고, 그 위치부터 다시 투입을 시작하기 때문에
    자연스럽게 이전 영역은 투입하지 않는다 => 조합 
    """
    for s in range(start_idx, D):
        # s : 선택한 행의 인덱스
        tmp_arr = matrix[s]
        matrix[s] = [0] * W
        if dfs(remain_cnt - 1, start_idx + 1):
            return True
        matrix[s] = [1] * W
        if dfs(remain_cnt - 1, start_idx + 1):
            return True
        matrix[s] = tmp_arr
    return False

# 주어진 입력 받기
T = int(input())
for tc in range(1, T + 1):
    # D: 보호필름 두께, W: 가로크기, K: 합격기준
    D, W, K = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(D)]
    min_inject_cnt = 0
    # 두께만큼 약품 투입 가능
    for inject_cnt in range(D + 1):
        if dfs(inject_cnt, 0):  # 남은 투입 횟수, 인덱스. 첫줄부터 돌려보기
            min_inject_cnt = inject_cnt  # 갱신
            break
    print(f"#{tc} {min_inject_cnt}")

##########################################
## 점심식사시간
import sys

sys.stdin = open("sample_input.txt", "r")

from collections import deque


# 자리부터 계단까지 거리 구하기
def get_dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# 계단 내려가는 중_계단 내 최대인원 3명_문제조건
def down_stairs(stair_on_list):
    for idx in range(3):
        # 내려가는 중이면 1씩 줄여주기. 0이 되면 끝
        if stair_on_list[idx] != 0:
            stair_on_list[idx] -= 1
    return stair_on_list


# 계단 진입시키기 함수
def place_people_on_stairs(waiting_queue, stair_on_list, stair_len, cnt_time):
    for stair_idx in range(3):
        # 계단을 내려가야하는 사람이 남았고, 시간이 충분히 흘러서 이미 도착했으며, 계단에 빈 자리가 있다면
        if waiting_queue and waiting_queue[0] <= cnt_time and stair_on_list[stair_idx] == 0:
            # 기다리는 사람 꺼내서 출발시키기
            pop_data = waiting_queue.popleft()
            if pop_data == cnt_time:
                # 방금 막 도착했다면 1초 기다리고 출발_문제조건
                stair_on_list[stair_idx] = stair_len + 1
            else:
                stair_on_list[stair_idx] = stair_len
    return


# 메인 함수
def dfs(idx, a_dist_list, b_dist_list):
    global min_time
    # 현재까지 최소 거리보다, 가장 늦게 도착한 사람 + 계단 길이인 경우에는 아래 로직을 계산하지 않음_가지치기
    if a_dist_list and min_time <= max(a_dist_list) + stair_list[0][2]:
        return
    if b_dist_list and min_time <= max(b_dist_list) + stair_list[1][2]:
        return
    # 모든 사람에 대해 확인했다면,
    if idx == len(people_list):
        # queue 구현해서 최종 시간에 따라 최소시간 갱신하기
        t = 0
        a_stair_on_list = [0] * 3
        b_stair_on_list = [0] * 3

        # 이미 계단 배정이 완료되었으니, 정렬_누구부터 내보낼지
        a_dist_list.sort()
        b_dist_list.sort()
        # 계단별로 큐 만들기
        a_queue = deque(a_dist_list)
        b_queue = deque(b_dist_list)

        # 사람이 남아있다면 계속 돌기
        while True:
            # 계단 내려가기 함수
            a_stair_on_list = down_stairs(a_stair_on_list)
            b_stair_on_list = down_stairs(b_stair_on_list)
            # 계단 진입시키기 함수
            place_people_on_stairs(a_queue, a_stair_on_list, stair_list[0][2], t)
            place_people_on_stairs(b_queue, b_stair_on_list, stair_list[1][2], t)
            # 첫둘 계단을 내려가는 중인 사람 없고, 첫둘계단을 기다리는 중인 사람이 없다면 끝
            if not a_queue and not b_queue and sum(a_stair_on_list) == 0 and sum(b_stair_on_list) == 0:
                break
            # 시간 +1
            t += 1
            if min_time <= t:
                return
        # 최소시간 갱신
        min_time = min(min_time, t)
        return
    # 선택한 사람을 첫번째 계단으로 보내기
    a_dist = get_dis(stair_list[0][:2], people_list[idx])
    dfs(idx + 1, a_dist_list + [a_dist], b_dist_list)
    # 선택한 사람을 두번째 계단으로 보내기
    b_dist = get_dis(stair_list[1][:2], people_list[idx])
    dfs(idx + 1, a_dist_list, b_dist_list + [b_dist])


# 주어진 입력 받기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    min_time = 999999

    # 사람 위치와 계단 위치 확인해주기
    people_list = []
    stair_list = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0:
                continue
            elif maps[i][j] == 1:
                people_list.append([i, j])  # 사람 좌표
            else:
                stair_list.append([i, j, maps[i][j]])  # 계단 좌표와 내려가는 시간
    # 메인 함수 실행
    dfs(0, [], [])
    # 출력하기
    print(f"#{tc} {min_time}")

###################################################
## 등산로 조성
import sys, pprint
sys.stdin = open("sample_input.txt", 'r')

def find_road(i, j, cnt, check):
    global already_fix, ans
    for dx, dy in dxy:
        nx, ny = i + dx, j + dy
        # 지도 범위를 넘어가면 안됨
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue
        # 계속계속 작아질거라서 체크는 없어도 되는걸까? 어차피 다음으로 나갔다면 되돌아올 수 없음. ㅏ 와서 공사할수도 있으니까, 안전상 체크ㅇ
        if check[nx][ny] != 0:
            continue
        # 이동하고자 하는 위치가 더 높으면 안됨
        if road_map[i][j] <= road_map[nx][ny]:
            # 선택지 1. 최대 K만큼 공사하고 진행하기 # 공사하는 선택지는 한번만 실행 가능.
            if road_map[nx][ny] - road_map[i][j] + 1 <= K and already_fix == False:
                # 공사할거면 already_fix를 True로 갱신
                already_fix = True
                cnt += 1
                check[nx][ny] = cnt
                temp = road_map[nx][ny]  # 원복에 사용하려고 기존 값 temp에 저장
                road_map[nx][ny] = road_map[i][j] - 1  # 공사
                # 다음 사방탐색
                ans = max(ans, cnt)
                find_road(nx, ny, cnt, check)
                cnt -= 1
                check[nx][ny] = 0
                road_map[nx][ny] = temp
                already_fix = False
            # 선택지 2. 안가기
            continue
        # 이동할 수 있는 상황이라면
        cnt += 1
        check[nx][ny] = cnt
        # 다음 사방탐색
        ans = max(ans, cnt)
        find_road(nx, ny, cnt, check)
        cnt -= 1
        check[nx][ny] = 0
    return ans

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
T = int(input())  # 총 테스트 케이스의 개수 T
for tc in range(1, 1+T):
    N, K = map(int, input().split())  # 지도의 한 변의 길이 N, 최대 공사 가능 깊이 K
    road_map = [list(map(int, input().split())) for _ in range(N)]  # N * N 크기의 지도 정보

    check = [[0]* N for _ in range(N)]

    # 정답은 가장 긴 등산로. max로 갱신하기 위해서 0으로 초기설정.
    ans = 0
    # 가장 높은 봉우리 찾기
    start = max(map(max, road_map))
    for i in range(N):
        for j in range(N):
            if road_map[i][j] == start:
                cnt = 1
                check[i][j] = cnt
                already_fix = False
                find_road(i, j, cnt, check)
                check[i][j] = 0

    print(f'#{tc} {ans}')

###############################################
## 차량정비소
from collections import deque


def chk_queue(chk):
    for ab, chk_time, customer in chk:
        if customer == '':
            return False
    return True


T = int(input())
for tc in range(1, T + 1):
    n, m, k, a_target, b_target, = map(int, input().split())
    CUSTOMER = ''

    # A창구
    a_list = list(map(int, input().split()))
    a_chk = [[a, 0, CUSTOMER] for a in a_list]
    a_queue = deque()
    # B창구
    b_list = list(map(int, input().split()))
    b_chk = [[b, 0, CUSTOMER] for b in b_list]
    b_queue = deque()

    t_map = map(int, input().split())
    t_queue = deque((i, t) for i, t in enumerate(t_map, start=1))

    waiting_for_receipt_queue = deque([])
    waiting_for_repair_queue = deque([])
    time = 0

    a_visited = {i + 1: set([]) for i in range(n)}
    b_visited = {i + 1: set([]) for i in range(m)}

    while True:
        # 접수 창구
        # if t_queue: print(t_queue[0][1], time)
        while t_queue and t_queue[0][1] == time:
            waiting_for_receipt_queue.append(t_queue.popleft())
            a_queue.append(1)

        for i, (a, chk_time, customer) in enumerate(a_chk):
            # 고객 번호 낮은 순 / 창구 번호 낮은 순
            if customer == '' and waiting_for_receipt_queue:
                a_chk[i][1] = a
                a_chk[i][2] = waiting_for_receipt_queue.popleft()[0]
                a_visited[i + 1].add(a_chk[i][2])

            # 작업 진행
            a_chk[i][1] -= 1

        for i, (a, chk_time, customer) in enumerate(a_chk):
            # 접수 처리가 끝난 고객 수리 대기열로
            # 먼저 기다리는 순
            # 동시에 왔을 경우 접수 창구 번호 낮은 순
            if chk_time == 0 and customer != '':
                waiting_for_repair_queue.append(customer)
                a_chk[i][1] = a
                a_chk[i][2] = ''
                a_queue.popleft()
                b_queue.append(1)

        # 정비 창구
        for i, (b, chk_time, customer) in enumerate(b_chk):
            # 여러 곳 비었을 경우, 정비 창구 번호 작은 순
            if customer == '' and waiting_for_repair_queue:
                b_chk[i][1] = b
                b_chk[i][2] = waiting_for_repair_queue.popleft()
                b_visited[i + 1].add(b_chk[i][2])

            # 작업 진행
            b_chk[i][1] -= 1

        for i, (b, chk_time, customer) in enumerate(b_chk):
            if chk_time == 0 and customer != '':
                b_chk[i][1] = b
                b_chk[i][2] = ''
                b_queue.popleft()

        if b_queue or a_queue or t_queue:
            time += 1
            continue
        break
    result = sum(a_visited[a_target].intersection(b_visited[b_target]))
    print(f"#{tc} {result if result else -1}")

############################################################
## 벽돌깨기
from collections import deque
from copy import deepcopy

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# BFS를 사용한 벽 지우기 시뮬레이션
def cal_wall(board, start_y, start_x):
    c_board = deepcopy(board)
    next_board = [[0] * len(board[0]) for _ in range(len(board))]
    # 큐 도는 동안 c_board 배열 손상시키기
    queue = deque([])
    queue.append((start_y, start_x, c_board[start_y][start_x]))
    c_board[start_y][start_x] = 0
    while queue:
        y, x, cnt = queue.popleft()
        # 2면 +1만 터져야하고, 3이어야 +1, +2가 터지기 때문
        for pos in range(1, cnt):
            for i in range(4):
                ny = y + dy[i] * pos
                nx = x + dx[i] * pos
                if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]):
                    continue
                if c_board[ny][nx] == 0:
                    continue
                queue.append((ny, nx, c_board[ny][nx]))
                c_board[ny][nx] = 0
    for idx_x in range(len(board[0])):
        cur_y = len(board) - 1
        for idx_y in range(len(board)):
            if c_board[len(board) - idx_y - 1][idx_x] != 0:
                next_board[cur_y][idx_x] = c_board[len(board) - idx_y - 1][idx_x]
                cur_y -= 1
    return next_board


# DFS를 사용한 공던지기 시뮬레이션
def try_ball(board, num, size_x, size_y):
    global min_cnt
    if num == 0:
        # 세고
        cnt = 0
        for li in board:
            for elem in li:
                if elem != 0:
                    cnt += 1
        min_cnt = min(min_cnt, cnt)
        return
    # 끝까지 오기 전에 다 깨진 경우
    if sum(board[size_y - 1]) == 0:
        min_cnt = 0
        return
    for start_x in range(size_x):
        # y좌표 찾기. 없으면 반환하기.
        start_y = -1
        for idx in range(size_y):
            if board[idx][start_x] != 0:
                # print(board[idx][start_x])
                start_y = idx
                break
        # 해당 줄에 공이 없을 때
        if start_y == -1:
            continue
        # 해당 좌표롤 기준으로 부순 board 반환받고
        result_board = cal_wall(board, start_y, start_x)
        try_ball(result_board, num - 1, size_x, size_y)

T = int(input())
for tc in range(1, T + 1):
    min_cnt = float("inf")
    num, size_x, size_y = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(size_y)]

    try_ball(board, num, size_x, size_y)

    print(f"#{tc} {min_cnt}")