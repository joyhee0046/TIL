import sys
sys.stdin = open('input (2).txt', 'r')

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    line_li = [list(map(int, input().split())) for _ in range(M)]

    # 거리 확인할 배열 생성
    check_li = [[99999, 99999] for _ in range(N+1)]
    # print(check_li)

    # 기본거리로 수정
    check_li[0] = [0, 0]
    check_li[X] = [0, 0]
    for st, end, c in line_li:
        if end == X:
            check_li[st][0] = c
        if st == X:
            check_li[end][1] = c
    # print(check_li)

    # 경유지역누적거리 + 이번 거리 계산해서 min으로 갱신
    # temp_0 = []
    # temp_1 = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            temp_0 = [check_li[j][0]]
            temp_1 = [check_li[j][1]]
            for st, end, c in line_li:
                if end == i:
                    cc = check_li[st][1]
                    temp_1.append(c+check_li[st][1])
                if st == i:
                    cc = check_li[end][0]
                    temp_0.append(c+check_li[end][0])
            check_li[i] = [min(temp_0), min(temp_1)]
            print(check_li)

    for i in range(N+1):
        check_li[i] = check_li[i][0] + check_li[i][1]

    # print(f"#{tc} {max(check_li)}")