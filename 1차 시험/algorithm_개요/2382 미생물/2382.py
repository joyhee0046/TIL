import sys
sys.stdin = open("sample_input.txt", 'r')


def want2know(x, y):
    global board

    # 이동할 칸 수 받기
    dx, dy = board[x][y][1]
    # nxy는 이동 후의 좌표
    nx, ny = x+dx, y+dy
    # 이동할 자리가 -1이라면, 약품처리칸.
    if board[nx][ny] == -1:
        board[nx][ny] = board[x][y][:]  # 기존 값을 옮겨주고
        board[nx][ny][0] = board[x][y][0]//2  # 미생물 수는 절반으로(나머지버림)
        board[nx][ny][1] = board[x][y][1]*-1  # 이동방향은 반대로
        board[nx][ny][2] -= 1   # 이동 시간 하나 줄이기
        board[x][y] = 0  # 기존 자리는 비워주기

    # 이동할 자리가 0이라면, 빈칸. 그대로 옮겨주기
    elif board[nx][ny] == 0:
        board[nx][ny] = board[x][y][:]
        board[nx][ny][2] -= 1
        board[x][y] = 0

    # 이동할 자리가 0도 아니고 -1도 아니라면, 다른 미생물이 들어있는 칸.
    ### 그 자리에 있는 미생물이 이미 움직인 친구인지 아닌지 확인해야 함.
    else:
        if board[nx][ny][2] < board[x][y][2]:
            if board[nx][ny][0] > board[x][y][0]:  # 기존과 이동할 군집 중 더 큰 군집에 수를 더하기
                board[nx][ny][0] += board[x][y][0]   # 큰 군집에 작은 군집 수 더하기
                board[nx][ny][2] -= 1
                board[x][y] = 0
            else:
                board[x][y][0] += board[nx][ny][0]
                board[nx][ny] = board[x][y][:]
                board[nx][ny][2] -= 1
                board[x][y] = 0
        else:
            board[x][y][2] -= 1
            tmp = [nx, ny, board[x][y][:]]
            temp.append(tmp)

    # 이전에 못옮긴 미생물이 있었는데, 얘가
    for i in range(len(temp)):
        if temp[i][x][y]:





# 테스트케이스만큼 확인하기
T = int(input())
for tc in range(1, T+1):
    # 보드크기, 실험시간, 군집수 입력받기
    N, M, K = map(int, input().split())
    # 0으로 채워진 보드를 만들고
    board = [[0]*N for _ in range(N)]
    # K만큼 반복하며 주어진 자리에 미생물수와 방향 저장
    for _ in range(K):
        x, y, cnt, way = map(int, input().split())
        # 사방 지정에 따라 x,y좌표 값으로 바꿔서 저장
        if way == 1: way = [-1, 0]
        if way == 2: way = [1, 0]
        if way == 3: way = [0, 1]
        if way == 4: way = [0, -1]
        board[x][y] = [cnt, way, M]
    # 약품처리된 공간 -1로 표시
    for i in range(N):
        board[0][i] = -1
        board[-1][i] = -1
        board[i][0] = -1
        board[i][-1] = -1

    # 기존 군집이 이동하지 않았는데, 그 자리에 가야할 때 사용할 임시 저장 리스트.
    temp = []

    # M시간 동안 반복
    for _ in range(M):
        # 보드판 전체를 돌면서 비었거나 약품처리 된 곳은 그냥 지나고 미생물이 있는 곳은 함수로 들어가기
        for idx_x in range(N):
            for idx_y in range(N):
                if board[idx_x][idx_y] == 0:
                    continue
                if board[idx_x][idx_y] == -1:
                    continue
                want2know(idx_x, idx_y)

    # 이동이 끝난 후 미생물 수 구하기
    ans = 0
    for idx_x in range(N):
        for idx_y in range(N):
            if board[idx_x][idx_y] != 0 and board[idx_x][idx_y] != -1:
                ans += board[idx_x][idx_y][0]

    #print(board)
    print(f"#{tc} {ans}")


#### 이동하고 싶은 자리에 이사시킨 보드를 아예 새로 만들어서,
#### 거기에 계산된 값도 넣고, 겹치는 친구도 나열했다가 계산하는 것이 정확할까?
#### 새 보드에서 계산하면서 기존 보드를 갱신하는 것. 새 보드는 기존 보드 카피.

#### 새로 짜는 김에 기범오빠가 알려준것처럼, for i, for j 로 전체행렬을 보지 않고
#### 위치를 정확하게 아니까 위치 리스트를 작성해서 in li로 확인하여 접근하는 것도!