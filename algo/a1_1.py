'''
N*N격자판 상에서 하강 모의실험을 한다. 격자판의 맨 위(제1행)에 있는 셀에 블록이 있으면 하강을 시도한다. 블록이 내려가다가 만나는 블록은 해당 블록이 포함된 블록덩어리의 무게만큼 저항력을 갖고 있다. 이 저항력을 이겨야 하강할 수 있다. 만일 힘이 부족하다면 그 자리에 멈춘다.
하나의 블록은 처음에 1의 힘으로 하강을 시도한다. 블록 또는 블록 덩어리는 한 칸을 하강할 때마다 힘이 1.9배가 된다. 두 칸을 내려가면 1.9*1.9로 3.61배가 된다. 4개의 블록으로 이루어진 덩어리가 3칸을 하강한 직후 이 덩어리의 힘(하강력)은 4*1.9*1.9*1.9로 27.4가 된다.
하강하는 과정에서 자리잡고 있는 장애물 즉, 블록 또는 블록덩어리는 덩어리의 크기(블록 수)만큼 저항력을 가지고 있다. 마주친 장애물이 수직으로 4칸인 경우의 저항력은 4이다.
4개로 이루어진 덩어리는 4를 초과하는 하강력이 주어져야 비로소 하강을 시작하고 그렇지 않으면 그 자리에서 버틴다. 블록들은 수직으로만 영향을 미칠 뿐 다른 열에 있는 블록에는 전혀 영향을 미치지 않는다.
블록 중 한 줄이
1
0
1
0

1
1
1
1
0
0
이라면
첫 블록이 하강을 시도하여 다음 블럭을 만나는 순간 힘이 1.9가 되어 1의 힘을 가지고 있는 블럭과 함께 하강한다.
블록 덩어리로 하강하다 4개짜리 블록장애물을 만나는데, 하강하는 덩어리의 힘은 2.9*1.9로 5.52의 힘을 가졌기 때문에 하강할 수 있다.
6개짜리 블럭덩어리가 바닥까지 내려갈 수 있다.

첫 줄에 존재하는 모든 블럭에 대해 하강을 적용했다면, 2차 하강을 진행한다.
2차하강은 중력을 오른쪽으로 작용시켜 블록을 이동시킨다(우측하강). 원리는 힘이 우측으로 작용할 뿐 계산원리는 1차 하강과 동일하다.
1차 하강의 조건과 동일하게 블럭들은 오른쪽으로만 영향을 미칠 뿐 다른 행에 있는 블록에는 전혀 영향을 미치지 않는다.
블록 중 한 줄이
1 0 0 0 1 0 1 0 0 0
이라면
첫 블럭이 하강하며 1*1.9*1.9*1.9의 힘을 가지고 첫 번째 장애물을 만나게 된다. 장애물의 힘보다 블럭덩어리의 힘이 더 세기 때문에 계속 진행한다.
결과적으로 3개짜리 블럭 덩어리가 오른쪽 바닥까지 하강하게 된다.

장애물들을 가진 N*N 격자판의 초기 상태가 주어질 때, 맨 윗줄에 있는 블록들을 동시에 하강시킨 후, 이 결과들로부터 맨 왼쪽열에 있는 블록들을 우측하강 시킨결과를 알아내는 python코드.
'''

import sys
sys.stdin = open('1_1.txt', 'r')

def calculate_forces(board, N):
    """블럭이 가지고 있는 힘계산
    목적: 각 셀의 아래 방향으로 존재하는 연속 블록의 개수를 계산.
    매개변수:
    board: 격자판 상태 (0은 빈 칸, 1은 블록).
    N: 격자 크기.
    출력: NForce, 각 셀의 수직 방향 저항력(연속 블록 개수).
    작동 방식:
    visited 배열로 이미 처리된 블록을 추적.
    각 셀에서 아래로 탐색하여 연속 블록의 개수를 계산.
    수직으로 연결된 블록 개수를 NForce[i][j]에 저장."""
    NForce = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    for i in range(1, N):
        for j in range(N):
            if not board[i][j] or visited[i][j]:
                continue
            tmpX, tmpY = i, j
            countNForce = 0
            while 0 <= tmpX < N and board[tmpX][tmpY]:
                visited[tmpX][tmpY] = True
                countNForce += 1
                tmpX += 1
            NForce[i][j] = countNForce

    return NForce


def update_board(board, N, NForce):
    """하강 수행. 보드 업데이트
    목적: 수직 하강 시뮬레이션을 수행하여 블록을 새로운 위치로 이동.
    매개변수:
    board: 격자판 상태.
    N: 격자 크기.
    NForce: 각 셀의 수직 방향 저항력.
    작동 방식:
    초기화:
    첫 행(board[0][i])에서 블록이 있는 위치를 초기화(power[i] = 1, weights[i] = 1).
    하강 시뮬레이션:
    각 열에 대해:
    현재 블록의 힘이 아래 블록의 저항력보다 크면 하강 가능.
    하강 중 블록의 힘은 1.9배로 증가, 하강한 블록의 개수(weights)도 증가.
    이동한 블록은 이전 위치(board[index - 1][j])에서 삭제하고 새로운 위치로 갱신.
    최종 갱신:
    남아 있는 블록 개수(weights)에 따라 격자판을 업데이트."""
    power = [0] * N
    weights = [0] * N
    indexes = [N + 1] * N

    for i in range(N):
        if board[0][i]:
            weights[i] = 1
            power[i] = 1
            indexes[i] = 0

    for index in range(1, N):
        for j in range(N):
            if indexes[j] < index - 1 or NForce[index][j] >= power[j]:
                continue
            board[index - 1][j] = 0
            if indexes[j] > index - 1: continue
            if NForce[index][j] == 0:
                indexes[j] = index
                power[j] *= 1.9
            else:
                weights[j] += NForce[index][j]
                power[j] += NForce[index][j]
                indexes[j] += NForce[index][j]

    for j in range(N):
        if indexes[j] == -1:
            continue
        tmpX = indexes[j]
        while weights[j]:
            board[tmpX][j] = 1
            weights[j] -= 1
            tmpX -= 1


def count_results(board, N):
    """바닥에 모인 덩어리 계산
    count_results(board, N)
    목적: 최종 상태에서 마지막 행과 마지막 열의 블록 개수를 계산.
    매개변수:
    board: 갱신된 격자판 상태.
    N: 격자 크기.
    출력:
    countA: 마지막 행의 블록 개수.
    countB: 마지막 열의 블록 개수."""
    countA, countB = 0, 0
    for i in range(N):
        if board[N - 1][i]:
            countA += 1
        if board[i][N - 1]:
            countB += 1
    return countA, countB


def process_board(board, N):
    """함수 실행시키기
    목적: 격자판에 대해 하강 시뮬레이션을 수행.
    매개변수:
    board: 격자판 상태.
    N: 격자 크기.
    작동 방식:
    calculate_forces를 호출해 각 셀의 저항력(NForce) 계산.
    update_board를 호출해 하강 시뮬레이션 수행.
    격자 상태를 출력(디버깅용)."""
    NForce = calculate_forces(board, N)
    # print("-----------------")
    # for row in range(N):
    #     print(*NForce[row])
    # print("-----------------")
    update_board(board, N, NForce)
    print("-----------------")
    for row in range(N):
        print(*board[row])
    print("-----------------")


# T = int(input())
for test_case in range(10):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 수평 방향 계산 및 갱신
    process_board(board, N)

    # 행렬을 전치하여 수직 방향을 수평 방향처럼 처리
    transposed_board = list(map(list, zip(*board)))
    process_board(transposed_board, N)

    # 전치된 행렬을 다시 원래대로 복원
    board = list(map(list, zip(*transposed_board)))

    # 최종 결과 계산
    countA, countB = count_results(board, N)
    print(f"#{test_case + 1} {countA} {countB}")