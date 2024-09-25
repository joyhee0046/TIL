N = int(input())
li = list(map(int, input().split()))
del_node = int(input())

graph = defaultdict(list)

del_parent = 0
for i in range(N):
    if li[i] == -1:
        continue
    if i == del_node:
        del_parent = li[i]
    graph[li[i]].append(i)

#print(graph)
check = {del_node}
graph[del_parent].remove(del_node)
# for i in graph[del_node]:
if graph[del_node]:
    q = deque(graph.pop(del_node))
    # check.add(i)
    while q:
        this_node = q.popleft()
        # 자식이 없을 경우 pop할 수 없음 -> 예외 처리
        if not graph[this_node]:
            # check.add(k)
            continue
        this_li = graph.pop(this_node)
        for k in this_li:
            q.append(k)
            check.add(k)

# print(graph)
leave_leaf = list(graph.values())
# print(leave_leaf)
# print(leaf)

least_leaf = set()
for i in range(len(leave_leaf)):

    if leave_leaf[i]:
        for k in leave_leaf[i]:
            least_leaf.add(k)
        check.add(i)

# print(least_leaf)
# print(check)
ans = least_leaf - check
# print(ans)
print(len(ans))