import sys
sys.stdin = open('sample_input.txt', 'r')

def find_set(x):
    if x != p[x]:  # 노드 x가 자기 자신을 부모로 가지지 않는 경우
        p[x] = find_set(p[x])  # 부모 노드를 재귀적으로 찾고 경로 압축 수행
    return p[x]

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

T = int(input())
for tc in range(1, 1 + T):
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
