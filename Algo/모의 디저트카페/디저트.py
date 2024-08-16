import sys
sys.stdin = open("sample_input.txt", 'r')


dxy = [[1, -1], [1, 1], [-1, 1], [-1, -1]]
def cafe_way(nnext):
    dx, dy = dxy[nnext]
    return dx, dy


def cafe_tour(start, take_list):
    global nnext, dx, dy, result
    nnext += 1
    dx, dy = cafe_way(nnext)
    x, y = start
    while True:
        nx, ny = dx+x, dy+y
        # 범위를 벗어나면
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break
        # 네모를 완성하면
        if [i,j] == [nx, ny]:
            result.append(len(take_list))
            return len(take_list)
        # 같은 디저트를 먹으면
        if cafe[nx][ny] in take_list:
            take_list=[ ]
            break
        take_list.append(cafe[nx][ny])
        x, y = nx, ny
        cafe_tour([x, y], take_list)
        nnext += 1
        dx, dy = cafe_way(nnext)

    return len(take_list)

# 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int,input().split())) for _ in range(N)]
    
    # 디저트를 가장 많이 먹을 수 있는 경우를 확인하기 위한 max값
    max_cafe = -1
    result = []
    # 시작점 정하는 이중for문
    for j in range(1, N-1):
        for i in range(0, N):
            nnext = -1
            take_list = [cafe[i][j],]
            ans = cafe_tour([i ,j], take_list)
            max_cafe = max(max_cafe, ans)
    # if max_cafe == 0:
        
    print(f"#{tc} {max_cafe}")
    # 카페리스트를 1~N-2까지 순화하면 됨. range(1,N-1)
    # 기준 출발 = [x,y] dxy = [-1,1],[1,1],[1,-1],[-1,-1] 좌하우상 으로 돌아보기
    # 같은 방향으로 최대 N-2번 갈 수 있음.
    # 무조건 모든 방향을 한번씩 사용해야 함.
    # 먹은 디저트는 set으로 중복 없도록 한다. set에 담고 len이 늘어나는지 확인
    # 아니면 이제 먹을 디저트 in 그동안 먹은 디저트리스트 이런식으로?
    # 끝점이 start와 일치하는지 검산

