# V개의 작업과 이들 간의 선행 관계가 주어질 때, 일을 끝낼 수 있는 작업 순서를 찾는 프로그램을 작성(작업 순서 전체를 작성)

from collections import defaultdict, deque  # defaultdict: 그래프 표현, deque: BFS에 사용`

def topological_sort(V, E, edges):
    """
    DAG(Directed Acyclic Graph)의 위상 정렬을 수행하는 함수.

    :param V: 정점의 개수 (1부터 시작하는 정수)
    :param E: 간선의 개수
    :param edges: 간선 정보를 나타내는 리스트 (짝수 크기, [a, b, ...] 형식)
    :return: 작업 순서를 저장한 리스트
    """
    # 그래프와 진입 차수 초기화
    graph = defaultdict(list)  # 그래프의 인접 리스트 표현
    in_degree = [0] * (V + 1)  # 각 노드의 진입 차수, 노드 번호는 1부터 시작
    result = []  # 위상 정렬 결과를 저장할 리스트

    # 그래프 구성 및 진입 차수 계산
    for i in range(E):
        a, b = edges[i * 2], edges[i * 2 + 1]  # 간선의 시작 노드(a), 끝 노드(b)
        graph[a].append(b)  # a에서 b로 향하는 간선을 그래프에 추가
        in_degree[b] += 1  # b의 진입 차수 증가

    # 진입 차수가 0인 모든 노드를 큐에 추가 (처음에 작업 가능한 노드들)
    queue = deque([v for v in range(1, V + 1) if in_degree[v] == 0])

    # BFS로 위상 정렬 수행
    while queue:
        current = queue.popleft()  # 큐에서 가장 앞의 노드를 꺼냄
        result.append(current)  # 해당 노드를 결과 리스트에 추가

        # 현재 노드에서 출발하는 모든 간선을 제거
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1  # 자식 노드의 진입 차수를 1 감소
            if in_degree[neighbor] == 0:  # 진입 차수가 0이 되면
                queue.append(neighbor)  # 큐에 추가하여 이후 처리

    return result  # 위상 정렬 결과 반환

# 10개의 테스트 케이스 처리
T = 10
for test_case in range(1, T + 1):
    # 입력 받기
    V, E = map(int, input().split())  # V: 정점 수, E: 간선 수
    edges = list(map(int, input().split()))  # 간선 정보를 일렬로 입력받음

    # 위상 정렬 실행
    result = topological_sort(V, E, edges)

    # 출력: 테스트 케이스 번호와 작업 순서
    print(f"#{test_case}", *result)
