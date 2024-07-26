# import sys
# from collections import deque
# sys.stdin = open("input.txt", "r")
#
# def restore_road(road, x, y, cnt):
#     global check_road
#
#     check_road[x][y] = 0
#     que = deque([(x,y)])
#     dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#     while que:
#         x, y = que.popleft()
#         for dx, dy in dxy:
#             nx, ny = x+dx, y+dy
#             if 0 > nx or nx >= N or 0 > ny or ny >= N:
#                 continue
#             if check_road[nx][ny] != -1:
#                 continue
#             check_road[nx][ny] = check_road[x][y]+road[nx][ny]
#             que.append((ny, ny))
#
#             if nx == N-1 and ny == N-1:
#                 return check_road[nx][ny]
#     return -1
#
#
#
#
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for tc in range(1, T + 1):
#     # 데이터 입력받기
#     N = int(input())
#     road = [list(map(int, input())) for _ in range(N)]
#     cnt = []
#     check_road = road[:][:]
#     ans = restore_road(road, 0, 0, cnt)
#
# print(ans)


##########################################################
################### 체크보드에 값을 저장하면 체크를 체크하는게 곤란
################### 큐에 값을 저장하고 체크는 체크만 하는걸로 새로


#
# import sys
# from collections import deque
# sys.stdin = open("input.txt", "r")
#
# def restore_road(road,N):
#
#     check_road = [[-1]*N for _ in range(N)]
#     check_time = [[0]*N for _ in range(N)]
#
#     check_road[0][0] = 0
#     que = deque([(0, 0, 0)])
#     dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#     while que:
#         x, y, time = que.popleft()
#
#         for dx, dy in dxy:
#             nx, ny = x+dx, y+dy
#             if 0 > nx or nx >= N or 0 > ny or ny >= N:
#                 continue
#             if check_road[nx][ny] != -1:
#                 continue
#             check_road[nx][ny] = 0
#             ntime = time + road[nx][ny]
#             check_time[nx][ny] = ntime
#             que.append((nx, ny, ntime))
#
#             if nx == N-1 and ny == N-1:
#                 return ntime
#     return -1
#
#
#
#
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for tc in range(1, T + 1):
#     # 데이터 입력받기
#     N = int(input())
#     road = [list(map(int, input())) for _ in range(N)]
#
#     ans = restore_road(road,N)
#
#     print(ans)

##########################################################
############################## 동일한 가중치만 계산할 수 있었음.
#########먼 경로의 가중치가 더 작아서 갱신해야 하는 경우 고려해야 함



import sys
from collections import deque
sys.stdin = open("input.txt", "r")

#ver1
# def restore_road(road,N):
#
#     check_road = [[-1]*N for _ in range(N)]
#     check_time = [[0]*N for _ in range(N)]
#
#     check_road[0][0] = 0
#     que = deque([(0, 0, 0)])
#     dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#     while que:
#         x, y, time = que.popleft()
#
#         for dx, dy in dxy:
#             nx, ny = x+dx, y+dy
#             if 0 > nx or nx >= N or 0 > ny or ny >= N:
#                 continue
#             if check_road[nx][ny] != -1 and check_time[nx][ny] <= time + road[nx][ny]:
#                 continue
#             check_road[nx][ny] = 0
#             ntime = time + road[nx][ny]
#             check_time[nx][ny] = ntime
#             que.append((nx, ny, ntime))
#
#             if nx == N-1 and ny == N-1:
#                 return ntime
#     return -1

#ver2
def restore_road(road,N):

    check_road = [[99]*N for _ in range(N)]

    check_road[0][0] = 0
    que = deque([(0, 0, 0)])
    dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while que:
        time, x, y = que.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue
            if check_road[nx][ny] <= time + road[nx][ny]:
                continue
            ntime = time + road[nx][ny]
            check_road[nx][ny] = ntime
            que.append((ntime, nx, ny))

            if nx == N-1 and ny == N-1:
                return ntime
    return check_road[-1][-1]


#ver3
# def restore_road(road, N):
#
#     check_road = [[99]*N for _ in range(N)]
#
#     check_road[0][0] = 0
#     keep = list[[0, 0, 0]]
#     dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#     while keep:
#         temp = keep.pop(0)
#         time, x, y = temp[0], temp[1], temp[3]
#
#         for dx, dy in dxy:
#             nx, ny = x+dx, y+dy
#             if 0 > nx or nx >= N or 0 > ny or ny >= N:
#                 continue
#             if check_road[nx][ny] < time + road[nx][ny]:
#                 continue
#             ntime = time + road[nx][ny]
#             check_road[nx][ny] = ntime
#             keep.append((ntime, nx, ny))
#             keep.sort()
#             keep(print())
#             if nx == N-1 and ny == N-1:
#                 return ntime
#     return -1





T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    # 데이터 입력받기
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]

    ans = restore_road(road, N)

    print(ans)
#######################################################
####################### BFS로는 경로의 특성을 저장할 수 없음.
####################### DFS로 코드짜보기
#
# import sys
# sys.stdin = open("input.txt", "r")
#
# def restore_road(x, y, time):
#
#     dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#     for dx, dy in dxy:
#         nx, ny = x+dx, y+dy
#         if 0 > nx or nx >= N or 0 > ny or ny >= N:
#             continue
#         if check_road[nx][ny] != -1:
#             continue
#         check_road[nx][ny] = 0
#         time = time + road[nx][ny]
#         check_time[nx][ny] = time
#
#         restore_road(nx, ny, time)
#         check_road[nx][ny] = -1
#
#         if nx == N-1 and ny == N-1:
#             timeli.append(check_time[nx][ny])
#
#
#
#
#
#
#     if x == N-1 and y == N-1:
#         return timeli
#
#
#
#
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for tc in range(1, T + 1):
#     # 데이터 입력받기
#     N = int(input())
#     road = [list(map(int, input())) for _ in range(N)]
#
#     check_road = [[-1] * N for _ in range(N)]
#     check_time = [[0] * N for _ in range(N)]
#     check_road[0][0] = 0
#     timeli = []
#
#     ans = restore_road(0, 0, 0)
#
#     print(timeli)