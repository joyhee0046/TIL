import sys
sys.stdin = open('sample_input.txt', 'r')

# import math
def check_weight(weight, cnt):
    global leftli, rightli
    # 추를 다 썼다면 끝, 경우의 수 높이고 리턴.
    if weight == []:
        cnt += 1
        return
    # 오른쪽이 더 무거워지면 안됨, 리턴.
    if sum(leftli) < sum(rightli):
        return

    for w in weight:
        if _ :


        check_weight(weight, cnt)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    weight = list(map(int, input().split()))

    # tt_check = (2**N)*(math.factorial(N))

    leftli = []
    rightli = []
    ans = check_weight(weight, 0)

    print(ans)