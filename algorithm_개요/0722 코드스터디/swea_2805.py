T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    start = N // 2
    end = N // 2

    result = 0
    # 가운데 줄 기준 윗부분 누적
    for i in range(N // 2):
        for j in range(start, end + 1):
            result += farm[i][j]
        start -= 1
        end += 1

    # 가운데 줄 전체 누적
    for i in range(N):
        result += farm[N // 2][i]

    # 가운데 기준 아래부분 누적
    for i in range(N // 2 + 1, N):
        start += 1
        end -= 1
        for j in range(start, end + 1):
            result += farm[i][j]

    print(f'#{test_case} {result}')