# 100개 中 31개
# 0-1과 1-0의 조합이 다른 결과를 가지는데, for문으로는 후순위를 처리할 수 없어서
# 재귀로 돌려야할 것 같다.

# import sys
# sys.stdin = open('input.txt', 'r')

import itertools

def calcul_vect(a, b):
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    vectx = ax - bx
    vecty = ay - by
    return vectx, vecty

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mapli = [list(map(int, input().split())) for _ in range(N)]
    mapli = sorted(mapli, key = lambda x: [x[1], x[0]])

    # 매칭할 수 있는 조합 찾기
    match = list(itertools.combinations([i for i in range(N)], 2))

    vect_li = []
    min_vect = 99999999999

    # 두 지렁이 사이의 벡터 구하기
    for i in match:
        cal = [i[0], i[1], calcul_vect(mapli[i[0]], mapli[i[1]])]
        cal2 = [i[1], i[0], calcul_vect(mapli[i[1]], mapli[i[0]])]
        if cal[2] == (0, 0):
            continue
        vect_li.append(cal)
        vect_li.append(cal2)
        # print(vect_li)

    # 어떤 조합이 최선일지 검정
    for i in range((N-1)*(N//2)):
        xsum_vect = 0
        ysum_vect = 0
        check_li = [False] * N
        # 이번 지렁이 짝 있다고 표시
        check_li[vect_li[i][0]] = True
        check_li[vect_li[i][1]] = True
        # 전체 벡터에 지금 벡터 더해주기
        xsum_vect += vect_li[i][2][0]
        ysum_vect += vect_li[i][2][1]
        for j in range(len(vect_li)):
            # 이미 짝이 있는 지렁이면 패스
            if check_li[vect_li[j][0]]:
                continue
            if check_li[vect_li[j][1]]:
                continue
            # 이번 지렁이 짝 있다고 표시
            check_li[vect_li[j][0]] = True
            check_li[vect_li[j][1]] = True
            # 전체 벡터에 지금 벡터 더해주기
            xsum_vect += vect_li[j][2][0]
            ysum_vect += vect_li[j][2][1]
            # print(check_li, xsum_vect, ysum_vect)
        # 전체 벡터의 최소값 찾기
        this_vect = xsum_vect * xsum_vect + ysum_vect * ysum_vect
        min_vect = min(min_vect, this_vect)
        # print(this_vect, min_vect)

    # 정답 출력
    print(f'#{tc} {min_vect}')