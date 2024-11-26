## 산악로봇
'''
N X N 크기의 산이 있다. 배열의 각 요소는 해당 위치의 높이를 나타냅니다.
산악로봇은 무조건 0,0 에서 출발하여 조난자가 있는 N-1,N-1에 도착해야 한다.
산악로봇은 상,하,좌,우 로만 이동할 수 있다.
현재 높이에서 같은 높이로 이동할때는 1의 연료가 필요하고, 낮은 높이로 이동할때는 0의 연료가 필요하다.
현재보다 더 높은 높이로 이동하게 되면 높이의 차이 * 2 만큼의 연료가 필요하다.
조난자를 구하기 위한 최소한의 연료를 구하라.
각 테스트 케이스의 첫번째 줄은 N, 다음줄 부터 N개 동안 산의 높이를 의미한다.
산의 높이는 0 ~ 9이며 4 <= N <= 30 이다
'''

from collections import deque
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def move():
    global ans
    queue = deque([(0, 0, arr[0][0], 0)])
    # visited = set()
    while queue:
        x, y, h, f = queue.popleft()

        if x == n-1 and y == n-1:
            ans = min(ans, f)
            continue

        for m in dxy:
            nx, ny = x + m[0], y + m[1]
            # if 0 <= nx < n and 0 <= ny < n and ((nx, ny) not in (visited | {(0, 0)}) or fuel[nx][ny] > f):
            if 0 <= nx < n and 0 <= ny < n and fuel[nx][ny] > f:
                if h > arr[nx][ny]:
                    nf = f
                elif h == arr[nx][ny]:
                    nf = f + 1
                else:
                    nf = f + (arr[nx][ny] - h)*2

                fuel[nx][ny] = nf
                # visited.add((nx, ny))2
                queue.append((nx, ny, arr[nx][ny], nf))


T = int(input())

for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = float('inf')
    fuel = [[float('inf')] * n for _ in range(n)]
    fuel[0][0] = 0
    move()

    print(f'#{tc+1}', ans)


'''
입력 예제
4
9 5 8 7
8 9 8 2
7 6 5 4
8 5 8 5
출력 예제
2

입력 예제2
6
1 1 1 1 1 1
9 9 9 9 9 1
9 9 1 1 1 1
9 9 1 9 9 9
9 9 1 1 1 1
9 9 9 9 9 1 
출력예제2
16
'''