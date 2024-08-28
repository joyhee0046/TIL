import sys
sys.stdin = open('sample_input.txt', 'r')


def find_set(x):
    if x != p[x]:  # 나의 부모 노드가 나 스스로가 아니면 ( 내가 대장이 아니면)
        # 대표자를 만날때까지 재귀적으로 들어가고
        # 대표자를 만나면 밖으로 함수를 나오면서 모두 대표자로 부모 인덱스를 업데이트
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:  # 다른 그룹이라면
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1


T = int(input())
for tc in range(1, T+1):
    # N = 전체 사람 번호
    # M = 제출된 쪽지의 수
    N, M = map(int, input().split())
    edge = list(map(int, input().split()))  # 간선 정보

    # make_set
    # disjoint set => 트리 형태로 관리를 할 거고,
    # 각 인덱스의 부모 인덱스를 저장하는 변수를 관리해야 한다.
    p = list(range(N+1))  # [0, 1 2, 3, 4, 5]
    rank = [0] * (N+1)  # union 랭크 비교용 리스트

    # 주어진 쪽지를 살펴보면서, union을 해준다.
    for i in range(M):
        x = edge[i*2]  # 지목하는 친구
        y = edge[i*2 + 1]  # 지목당하는 친구
        union(x, y)  # 그룹으로 묶기

    # 결국 원하는건 그룹의 개수
    # 그룹의 개수 => 대표자의 개수
    for i in range(1, N+1):
        p[i] = find_set(i)

    print(f'#{tc} {len(set(p)) - 1}')
