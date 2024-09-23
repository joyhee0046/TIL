import sys
sys.stdin = open('14719.txt', 'r')

T = int(input())

for tc in range(T):
    # 입력받기
    H, W = map(int, input().split())
    li = list(map(int, input().split()))

    leastdeep = 0
    deep = 0
    ans = 0

    # 왼부터 빗물 깊이 계산해보기
    for i in range(W):
        if li[i] > leastdeep:
            leastdeep = li[i]
            k = i
        ans += (leastdeep - li[i])
    # 고인 빗물이 없으면 끝!
    if ans == 0:
        flag = False
    else:
        # 있으면 반대벽 잘 찾았는지 검사
        flag = True
    while flag:
        # 갈수록 깊어지는 케이스라면 할거없음
        if li[i] != leastdeep:
            # 아니라면 뒤부터 돌면서 꼭대기 찾기
            for i in range(W-1,0,-1):
                if li[i] == leastdeep:
                    check = li[i+1:]
                    deep = max(check)
                    if max(check) == li[-1]:
                        ans -= ((W - i - 1) * (leastdeep - deep))
                        flag = False
                        break
                    leastdeep = max(check)
                    ans -= ((W - i - 1) * (check[1] - check[i - 1]))
                    if i == k:
                        flag = False
                        break

    flag = False
    break

    print(ans)