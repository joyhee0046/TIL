import sys
sys.stdin = open("sample_input.txt", "r")


def dfs(cx, cy, mv_dir, visited_desert):
    global max_shop_cnt

    # 시작 지점(si, sj) = 현재 지점(cx, cy) 과 같고, 방향이 3  => 최고 방문 가게 수를 갱신
    if [s_i, s_j] == [cx, cy] and mv_dir == 3:
        max_shop_cnt = max(max_shop_cnt, len(visited_desert))
        return

    # 내가 가게의 절반을 돌았는데, 현재까지 저장된 최대 디저트 개수의 절반도 못먹었다? 가지치기
    if mv_dir == 2 and max_shop_cnt >= len(visited_desert) * 2:
        return

    # 좌표 범위를 벗어났는 지 확인
    if cx < 0 or cx >= N or cy < 0 or cy >= N: return

    # 지금 방문한 가게의 디저트를 섭취한 경우
    if arr[cx][cy] in visited_desert: return

    # 현재 위치 방문 처리
    visited_desert.add(arr[cx][cy])

    # 현재 방향에 따라서 이동한다.
    nx, ny = cx + dxy[mv_dir][0], cy + dxy[mv_dir][1]

    dfs(nx, ny, mv_dir, visited_desert)  # 현재 방향을 유지한 채로 보내고

    if mv_dir < 3:  # 오른쪽 윗 대각선이 아니라면, 방향을 꺾어서 진행한다.
        dfs(nx, ny, mv_dir + 1, visited_desert)  # 현재 방향에서 꺾은 채로 보낸다.

    # 현재 위치의 방문 처리를 취소해야한다.
    visited_desert.remove(arr[cx][cy])

# 0: 오른쪽 대각선 아래, 1: 왼쪽 아래 대각선, 2: 왼쪽 위 대각선, 3: 오른쪽 위 대각선
dxy = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_shop_cnt = -1

    for s_i in range(N - 2):  # 행을 나타내고, 마지막 2개의 행은 돌지 않는다._마름모로 돌아야 해서_문제조건
        for s_j in range(1, N - 1):  # 열은 나타내고, 첫 번째 열은 돌지 않는다._마름모로 돌아야 해서_문제조건
            dfs(s_i, s_j, 0, set())  # 시작좌표, 방향, 먹은 디저트

    print(f"#{tc} {max_shop_cnt}")