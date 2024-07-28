from collections import deque
def bfs(graph, start):
    nodes = list(graph.keys9)
    visited = [Flase]*len(nodes)
    queue = deque([start])
    result = []
    start_index = nodes.index(start)
    visited[start_index] = True
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            neighbor_index = nodes.index(neighbor)
            if not visited[neighbor_index]:
                queue.append(neighbor)
                visited[neighbor_index] = True
    return result