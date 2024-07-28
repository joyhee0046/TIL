import sys

sys.stdin = open("sample_input.txt", 'r')

def want2know(x, y):
    global board, next_board, temp

    # 이동할 칸 수 받기
    cnt, way, M = board[x][y][0], board[x][y][1], board[x][y][2]
    print(cnt)
    dx, dy = way[0], way[1]
    # nxy는 이동 후의 좌표
    nx, ny = x + dx, y + dy
    # 이동할 자리가 -1이라면, 약품처리칸.
    if board[nx][ny] == -1:
        board[x][y][0] //= 2  # 미생물 수는 절반으로(나머지버림)
        board[x][y][1][1] *= -1  # 이동방향은 반대로
        board[x][y][1][0] *= -1
        board[x][y][2] -= 1  # 이동 시간 하나 줄이기
        next_board[nx][ny] = board[x][y] # 다음 시간에 저장
        board[x][y] = 0
        print(next_board[nx][ny])

    # 이동할 자리가 0이라면, 빈칸. 그대로 옮겨주기
    elif board[nx][ny] == 0:
        board[x][y][2] -= 1
        next_board[nx][ny] = board[x][y][:]  # 다음 시간에 저장
        board[x][y] = 0
        print(next_board[nx][ny])

    # 이동할 자리가 0도 아니고 -1도 아니라면, 다른 미생물이 들어있는 칸.
    else:
        # 나중에 모이는 미생물끼리 계산할 수 있도록 조정
        temp = 1
        board[x][y][2] -= 1
        next_board[nx][ny].append(list(board[x][y][:]))
        next_point.append([nx, ny])
        board[x][y] = 0
        print(next_board[nx][ny])

def board_fix():
    # 확인해야 할 지점의 값을 리스트로 뽑았다가
    for i in range(len(next_point)):
        x, y = next_point[i][0], next_point[i][1]
        tmp_li = []
        tmp_li.append(next_board[x][y])
        # 뽑은 리스트 중 가장 큰 값_([미생물수, 방향, 이동시간]으로 되어있음)을 기준으로 해야 하니까 미생물수 기준으로 내림차순 정렬
        tmp_li.sort(reverse=True)
        # 가장 큰 값인 리스크 첫번째 미생물수에 나머지 미생물 수 더하기
        for i in range(1, len(tmp_li)):
            tmp_li[0][0] += tmp_li[i][0]
        # 계산 완료된 내용으로 다음시간에 저장
        next_board[x][y] = tmp_li[0]


# 테스트케이스만큼 확인하기
T = int(input())
for tc in range(1, T + 1):
    # 보드크기, 실험시간, 군집수 입력받기
    N, M, K = map(int, input().split())
    # 0으로 채워진 보드를 만들고
    board = [[0] * N for _ in range(N)]
    # 미생물 위치 저장할 리스트 만들기
    point = [0]*K
    # K만큼 반복하며 주어진 자리에 미생물수와 방향 저장
    for i in range(K):
        x, y, cnt, way = map(int, input().split())
        # 사방 지정에 따라 x,y좌표 값으로 바꿔서 저장
        if way == 1: way = [-1, 0]
        if way == 2: way = [1, 0]
        if way == 3: way = [0, 1]
        if way == 4: way = [0, -1]
        board[x][y] = [cnt, way, M]
        # 미생물 군집 위치 저장
        point[i] = [x, y]

    # 약품처리된 공간 -1로 표시
    for i in range(N):
        board[0][i] = -1
        board[-1][i] = -1
        board[i][0] = -1
        board[i][-1] = -1

    # M시간 동안 반복
    for _ in range(M):
        # 다음 시간의 동작을 저장할 넥스트보드 만들고
        next_board = [[[0],[0]] * N for _ in range(N)]
        next_point = []
        temp = 0
        # 포인트에 있는 미생물 위치 받아서 함수 들어가기
        for idx_x, idx_y in point:
            want2know(idx_x, idx_y)
        if temp == 1:
            board_fix()
        board = next_board.copy()


    # 이동이 끝난 후 미생물 수 구하기
    ans = 0
    for idx_x in range(N):
        for idx_y in range(N):
            if board[idx_x][idx_y] != 0 and board[idx_x][idx_y] != -1:
                ans += board[idx_x][idx_y][0]

    # print(board)
    print(f"#{tc} {ans}")