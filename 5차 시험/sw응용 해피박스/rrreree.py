T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(M)]
    box_size = [0] * (N + 1)

    for i in range(M):
        for j in range(N, temp[i][0] - 1, -1):
            box_size[j] = max(box_size[j], box_size[j - temp[i][0]] + temp[i][1])

    print(f'#{test_case} {box_size[N]}')