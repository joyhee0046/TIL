import sys
sys.stdin = open('sample_input.txt', 'r')

def find_road(x, y):
    for dx, dy in dxy:
        nx, ny = dx+x, dy+y
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue

    pass

# 주어진 입력받기
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    m_li = [list(map(int, input().split())) for _ in range(N)]
    # 방문 확인할 리스트 만들기
    check_li = [[0 for _ in range(N)]for _ in range(N)]
    # 등산로가 시작될 자리 찾기
    st = max(map(max, m_li))

    for i in range(N):
        for j in range(N):
            if m_li[i][j] == st:
                find_road(i, j)
    print(st)