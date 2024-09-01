import sys
sys.stdin = open('sample_input.txt')


from collections import deque
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 델타탐색 ( 4방향 탐색)

# depth: 던진 블럭 개수 숫자
# broken_cnt: 현 시점까지 부순 블럭의 개수
# matrix : 현 시점까지 깨지고 남은 블럭 matrix
def dfs(depth, broken_cnt, matrix):
    global total_broken_block_cnt
    # 이미 결과가 나온 경우 => 주어진 블럭을 다 깨부순 경우의 수가 나온 경우에는 DFS 전체를 리턴
    if total_broken_block_cnt == total_block_cnt: return
    #  아직 구슬을 다 쏘기 전에  모든 블럭이 벌써 다 깨졋어... => 더 이상 할 필요가 없다.
    if broken_cnt == total_block_cnt:
        total_broken_block_cnt = broken_cnt
        return
    # 구슬을 다 쏜 경우_정답 갱신하고 종료
    if depth == N:
        total_broken_block_cnt = max(total_broken_block_cnt, broken_cnt)
        return
    # 모든 열에 블럭을 던지기
    for w in range(W):
        # 기존 블록판을 하나 복사해서 복사판을 부수고, 복사판을 DFS로 넘긴다. ( 이렇게하면 원본을 굳이 복구할 필요가 없음)
        arr = [x[:] for x in matrix]  # deepcopy
        # BFS로 부수기
        queue = deque()
        # 이번 회차에서 부순 벽돌의 개수를 저장할 변수
        tmp_broken_cnt = 0
        # 블록을 놓는 열에서 가장 맨 위에 있는 블록을 큐에 집어넣음
        for h in range(H):
            if arr[h][w]:  # 블럭이 존재하면, 큐에 집어넣고 for loop 탈출
                queue.append((h,w))
                break
        if not queue: continue  # 큐에 아무것도 없다. ( 해당 열에 블럭이 아무것도 존재하지 않는다. )

        # 큐가 빌 때까지 하나씩 꺼내서 부수기.
        while queue:
            x, y = queue.popleft()
            boom_cnt = arr[x][y]  # 벽돌의 수
            arr[x][y] = 0  # 꺼낸 벽돌이 부셔졌으니까, 0으로 빈공간으로 만든다.
            tmp_broken_cnt += 1  # 터진 벽돌 개수 추가
            for dx, dy in dxy:
                for dist in range(boom_cnt):
                    nx, ny = x + (dx * dist), y + (dy * dist)
                    # 좌표 검사, 범위를 벗어나면 같은 방향으로는 더 탐색하지 않음
                    if 0 > nx or H <= nx or 0 > ny or W <= ny: break
                    # 빈 곳인 경우에는 queue 에 추가하지 않을 거다.
                    if arr[nx][ny] == 0: continue
                    # 이미 큐에 들어있는 경우에는 추가 X
                    if (nx, ny) in queue: continue
                    # 부서진 블럭은 다시 큐에 삽입
                    queue.append((nx, ny))

        for j in range(W):  # 모든 열에 대해서
            stack = []
            # 맨 위에서 내려가면서 블럭을 스택에 추가
            for i in range(H):
                if not arr[i][j]: continue
                stack.append(arr[i][j])
                arr[i][j] = 0
            # 맨 아래에서 올라오면서 블럭을 스택에서 pop
            for i in range(H-1, H - len(stack) - 1, -1):
                arr[i][j] = stack.pop()
            # 다음 구슬을 놓고, 이번 라운드에서 깬 블럭 수와 변경된 블록판을 건네준다.
            dfs(depth + 1, broken_cnt + tmp_broken_cnt, arr)


T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())  # 던질 수 있는 블럭 수, 주어진 사각형 너비/높이
    matrix = [list(map(int, input().split())) for _ in range(H)]  # 주어진 2차원 배열
    # 결과값_최대한 많은 블럭 부수기
    total_broken_block_cnt = 0
    # 주어진 매트릭스의 총 벽돌 개수 카운트
    total_block_cnt = 0

    # 전체배열 돌면서 전체블럭 수 구하기
    for r in range(H):
        for c in range(W):
            if matrix[r][c]:
                total_block_cnt += 1

    dfs(0, 0, matrix)  # 몇번시도, 부서진블럭수, 배열

    # 전체블럭-제거블럭해서 정답_남은블럭_ 구하기
    ans = total_block_cnt - total_broken_block_cnt
    print(f'#{test_case} {ans}')