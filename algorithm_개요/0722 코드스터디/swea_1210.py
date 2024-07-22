T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착점 찾기
    end_r = 99
    end_c = 0

    for i in range(100):
        if ladder[99][i] == 2:
            end_c = i

    # 도착점부터 거슬러 올라가기
    # ladder[end_r][end_c] -> 도착점
    while end_r != 0:
        # 왼쪽 오른쪽에 사다리가 있는지 체크
        if 0 <= end_c + 1 <= 99 and ladder[end_r][end_c+1]:
            while end_c + 1 <= 99 and ladder[end_r][end_c+1]:
                end_c += 1
            end_r -= 1

        elif 0 <= end_c - 1 <= 99 and ladder[end_r][end_c-1]:
            while end_c - 1 <= 99 and ladder[end_r][end_c-1]:
                end_c -= 1
            end_r -= 1

        else:
            end_r -= 1

    print(f'#{test_case} {end_c}')