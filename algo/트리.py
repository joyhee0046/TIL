import sys
sys.stdin = open('1068.txt', 'r')

# from collections import defaultdict, deque
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     li = list(map(int, input().split()))
#     del_node = int(input())
#
#     graph = defaultdict(list)
#     for i in range(N):
#         if li[i] == -1:
#             continue
#         graph[li[i]].append(i)
#
#     #print(graph)
#     check = {del_node}
#     for i in graph[del_node]:
#         q = deque(graph.pop(del_node))
#         check.add(i)
#         while q:
#             this_node = q.popleft()
#             this_li = graph.pop(this_node)
#             for k in this_li:
#                 q.append(k)
#                 check.add(k)
#     # print(graph)
#     leave_leaf = list(graph.values())
#     # print(leaf)
#     least_leaf = set()
#     for i in range(len(leave_leaf)):
#         if leave_leaf[i]:
#             for k in leave_leaf[i]:
#                 least_leaf.add(k)
#             check.add(i)
#     # print(least_leaf)
#     # print(check)
#     ans = least_leaf - check
#     print(len(ans))
#
#
#
# ################런타임 에러 (NameError)##################



from collections import defaultdict, deque
T = int(input())
for tc in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    del_node = int(input())

    graph = defaultdict(list)
    for i in range(N):
        if li[i] == -1:
            continue
        graph[li[i]].append(i)

    check = {del_node}
    k = 0
    for i in graph[del_node]:
        q = deque(graph[del_node])
        check.add(i)
        graph[del_node] = []
        while q:
            this_node = q.popleft()
            for k in graph[this_node]:
                q.append(k)
                check.add(k)
            graph[this_node] = []

    leave_leaf = list(graph.values())
    least_leaf = set()
    for i in range(len(leave_leaf)):
        if leave_leaf[i]:
            for k in leave_leaf[i]:
                least_leaf.add(k)
    ans = least_leaf - check
    print(len(ans))