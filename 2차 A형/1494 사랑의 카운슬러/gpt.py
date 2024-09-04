import sys
sys.stdin = open('input.txt', 'r')

import itertools

def calcul_vect(ax, ay ,bx, by):
    vectx = ax - bx
    vecty = ay - by
    return vectx, vecty

# def match_how():


# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mapli = [list(map(int, input().split())) for _ in range(N)]

    # 매칭할 수 있는 조합 찾기
    match = list(itertools.combinations([i for i in range(N)], N//2))

    # print(match)

    # 전체 x와 전체 y구하기
    tt_x = 0
    tt_y = 0
    for i in range(N):
        tt_x += mapli[i][0]
        tt_y += mapli[i][1]

    # vectx = 0
    # vecty = 0
    vect_li = []
    min_vect = 99999999999


    # 어떤 조합이 최선일지 검정
    for i in range(len(match)//2):
        ax, ay = 0, 0
        for j in range(N//2):
            ax += mapli[i+j][0]
            ay += mapli[i+j][1]

    for i in range(len(match) // 2):
        ax, ay = 0, 0
        for j in range(N // 2):
            ax += mapli[i + j][0]
            ay += mapli[i + j][1]
        # print(ax, ay)
        bx = tt_x - ax
        by = tt_y - ay
        # print(bx, by)
        vectx, vecty = calcul_vect(ax, ay, bx, by)
        # print(vectx, vecty)
        this_vect = vectx * vectx + vecty * vecty
        # print(this_vect)
        min_vect = min(min_vect, this_vect)
        # print(min_vect)
        ax, ay = 0, 0
        for j in range(N // 2):
            ax += mapli[i + j][1]
            ay += mapli[i + j][0]
        # print(ax, ay)
        bx = tt_x - ax
        by = tt_y - ay
        # print(bx, by)
        vectx, vecty = calcul_vect(ax, ay, bx, by)
        # print(vectx, vecty)
        this_vect = vectx * vectx + vecty * vecty
        # print(this_vect)
        min_vect = min(min_vect, this_vect)
        # print(min_vect)
        # bx = ax - tt_x
        # by = ay - tt_y
        # print(bx, by)
        # vectx, vecty = calcul_vect(ax, ay, bx, by)
        # print(vectx, vecty)
        # this_vect = vectx * vectx + vecty * vecty
        # print(this_vect)
        # min_vect = min(min_vect, this_vect)


        # for j in range(i, len(match)):
        #     # 이미 짝이 있는 지렁이면 패스
        #     for k in range(N//2):
        #         if check_li[match[j][k]]:
        #             break
        #
        #     for k in range(len(match[j])):
        #         # 이번 지렁이 짝 있다고 표시
        #         check_li[match[j][k]] = True
        #         vectx += mapli[match[j][k]][0]
        #         vecty += mapli[match[j][k]][1]
        #     if ax != 0 and ay != 0:
        #         break
        #     ax, ay = vectx, vecty


        # print(vectx, vecty)
        # print(check_li)
        # this_vect = vectx * vectx + vecty * vecty
            # 전체 벡터에 지금 벡터 더해주기
            # xsum_vect += vect_li[j][2][0]
            # ysum_vect += vect_li[j][2][1]
            # print(check_li, xsum_vect, ysum_vect)
        # 전체 벡터의 최소값 찾기
        # this_vect = xsum_vect * xsum_vect + ysum_vect * ysum_vect
        # min_vect = min(min_vect, this_vect)
        # print(this_vect, min_vect)

    # 정답 출력
    print(f'#{tc} {min_vect}')