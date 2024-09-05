## 시간초과

import sys
sys.stdin = open('input.txt', 'r')

import itertools

def calcul_vect(a, b):
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    vectx = ax - bx
    vecty = ay - by
    return vectx, vecty

def match_how(vect_li, n, check_li, xsum_vect=0, ysum_vect=0):
    global min_vect
    tmp_chk = check_li[:]
    if n == 0:
        # 전체 벡터의 최소값 찾기
        this_vect = xsum_vect * xsum_vect + ysum_vect * ysum_vect
        min_vect = min(min_vect, this_vect)
        # print(xsum_vect, ysum_vect)
        return

    for i in range(len(vect_li)):
        if tmp_chk[vect_li[i][0]]:
            continue
        if tmp_chk[vect_li[i][1]]:
            continue
        tmp_chk[vect_li[i][0]] = True
        tmp_chk[vect_li[i][1]] = True

        match_how(vect_li[i+1:], n-1, tmp_chk, xsum_vect+vect_li[i][2][0], ysum_vect+vect_li[i][2][1])

        tmp_chk[vect_li[i][0]] = False
        tmp_chk[vect_li[i][1]] = False


# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mapli = [list(map(int, input().split())) for _ in range(N)]

    # 매칭할 수 있는 조합 찾기
    match = list(itertools.combinations([i for i in range(N)], 2))

    #
    # vectx = []
    # vecty = []
    vect_li = []
    min_vect = 99999999999
    # xsum_vect = 0
    # ysum_vect = 0
    # check_li = [False] * N

    # 두 지렁이 사이의 벡터 구하기
    for i in match:
        cal = [i[0], i[1], calcul_vect(mapli[i[0]], mapli[i[1]])]
        cal2 = [i[1], i[0], calcul_vect(mapli[i[1]], mapli[i[0]])]
        if cal[2] == (0, 0):
            continue
        vect_li.append(cal)
        vect_li.append(cal2)
        # print(vect_li)

    comb_list = match_how(vect_li, N//2, [False]*N)

    # 정답 출력
    print(f'#{tc} {min_vect}')