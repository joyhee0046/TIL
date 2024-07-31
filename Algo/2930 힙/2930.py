import sys
sys.stdin = open("sample_input.txt", 'r')


def heap_append(item, idx):
    heap.append(item)  # 새로운 요소를 리스트의 끝에 추가
    parent = (idx - 1) // 2  # 부모 노드의 인덱스 계산
    while idx > 0 and heap[idx] < heap[parent]:
        heap[idx], heap[parent] = heap[parent], heap[idx]  # 자식이 부모보다 작은 경우 교환
        idx = parent  # 인덱스를 부모로 업데이트
        parent = (idx - 1) // 2  # 새로운 부모 인덱스 계산


def heap_pop(heap, idx):
    if len(heap) == 0:
        return -1  # 힙이 비어 있는 경우 예외 발생
    if len(heap) == 1:
        return heap.pop()  # 힙에 요소가 하나만 있는 경우 그 요소를 반환
    root = heap[0]  # 루트 요소 저장
    heap[0] = heap.pop()  # 마지막 요소를 루트로 이동
    n = len(heap)
    smallest = idx  # 가장 작은 요소의 인덱스 초기화
    left = 2 * idx + 1  # 왼쪽 자식의 인덱스 계산
    right = 2 * idx + 2  # 오른쪽 자식의 인덱스 계산
    if left < n and heap[left] < heap[smallest]:
        smallest = left  # 왼쪽 자식이 현재 가장 작은 요소보다 작은 경우 업데이트
    if right < n and heap[right] < heap[smallest]:
        smallest = right  # 오른쪽 자식이 현재 가장 작은 요소보다 작은 경우 업데이트
    if smallest != idx:
        heap[idx], heap[smallest] = heap[smallest], heap[idx]  # 부모와 자식을 교환
        heap_pop(smallest, idx)  # 자식 노드에 대해 재귀적으로 sift-down 연산 수행
    return root  # 제거된 루트 요소 반환

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = []
    ans = []
    for _ in range(N):
        info = list(map(int, input().split()))


        if len(info) == 1:
            heap_pop(heap, info)
        else:
            heap_append(heap, info[1])

    print(f"#{tc}",*ans)

























# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     heap = []
#     ans = []
#     for _ in range(N):
#         info = list(map(int, input().split()))
#
#         if len(info) == 1:
#             # pop
#             if heap:
#                 ans.append(heap.pop(0))
#             else :
#                 ans.append(-1)
#         else:
#             # 삽입
#             heap.append(info[1])
#             if heap[(len(heap)-1)//2] >= heap[-1]:
#                 pass
#             else:
#                 temp = heap[(len(heap)-1)//2]
#                 heap[(len(heap)-1)//2] = heap[-1]
#                 heap[-1] = temp
#
#     print(f"#{tc}",*ans)