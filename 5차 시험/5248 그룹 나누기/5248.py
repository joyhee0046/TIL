import sys
sys.stdin = open('sample_input.txt', 'r')
#
# def find_set(x):
#     if x != p[x]:  # 노드 x가 자기 자신을 부모로 가지지 않는 경우
#         p[x] = find_set(p[x])  # 부모 노드를 재귀적으로 찾고 경로 압축 수행
#     return p[x]
#
# def union(x, y):
#     px = find_set(x)  # 노드 x의 대표자(부모) 찾기
#     py = find_set(y)  # 노드 y의 대표자(부모) 찾기
#     if px != py:  # 두 노드가 서로 다른 집합에 속해 있는 경우에만 합침
#         if rank[px] > rank[py]:  # 랭크가 높은 트리에 붙임
#             for i in p:
#                 temp = i.replace(px, py)
#                 result_list.append(temp)
#         elif rank[px] < rank[py]:
#             cnt = p.count(px)
#             for i in range(cnt):
#                 p[px] = py
#         else:
#             p[py] = px  # 랭크가 같은 경우 하나를 다른 하나의 부모로 설정
#         rank[px] += 1  # 랭크 증가


# def union(x, y):
#     px = find_set(x)  # 노드 x의 대표자(부모) 찾기
#     py = find_set(y)  # 노드 y의 대표자(부모) 찾기
#     if px != py:  # 두 노드가 서로 다른 집합에 속해 있는 경우에만 합침
#         if rank[px] > rank[py]:  # 랭크가 높은 트리에 붙임
#             cnt = p.count(py)
#             for i in range(cnt):
#                 p[py] = px
#         elif rank[px] < rank[py]:
#             cnt = p.count(px)
#             for i in range(cnt):
#                 p[px] = py
#         else:
#             p[py] = px  # 랭크가 같은 경우 하나를 다른 하나의 부모로 설정
#         rank[px] += 1  # 랭크 증가
#
# T = int(input())
# for tc in range(1, 1 + T):
#     N, M = map(int, input().split())
#     li = list(map(int, input().split()))
#     p = [str(i) for i in range(0, 1 + N)]  # 부모 노드 리스트 초기화
#     rank = [0] * (N + 1)  # 랭크 리스트 초기화
#
#     for i in range(0, len(li), 2):
#         union(li[i], li[i+1])
#
#     print(f'#{tc} {len(set(p))-1}')

# # T = int(input())
# # for tc in range(1, 1 + T):
# #     N, M = map(int, input().split())
# #     li = list(map(int, input().split()))
# #     group = [[i] for i in range(0, 1 + N)]
# #     for i in range(0, len(li), 2):
# #         for j in range(N):
# #             if li[i] in group[j]:
# #                 group[j].append(li[i + 1])
# #                 group[li[i+1]] = []
# #                 print(group)
# #                 break
# #             if li[i+1] in group[j]:
# #                 group[j].append(li[i])
# #                 group[li[i]] = []
# #                 print(group)
# #                 break
# #     group[0] = []
# #     cnt = 0
# #     for i in range(N+1):
# #         if group[i]:
# #             cnt += 1
# #     print(f'#{tc} {cnt}')

T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    group = [[i] for i in range(0, 1 + N)]
    for i in range(0, len(li), 2):
        for j in range(N):
            if li[i] in group[j]:
                group[j] += group[li[i + 1]]
                group[li[i+1]] = []
                break
            if li[i+1] in group[j]:
                group[j] += group[li[i]]
                group[li[i]] = []
                break
    cnt = -1
    for i in range(N+1):
        if group[i]:
            cnt += 1
    print(f'#{tc} {cnt}')