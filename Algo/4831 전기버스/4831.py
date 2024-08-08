import sys
sys.stdin = open("sample_input.txt", 'r')

def charge(start):
    global cnt
    # 마지막 충전을 했다면
    if start+K >= N:
        return cnt
    # 가장 멀리까지 가서 충전하고 재귀
    for chance in range(start+K, start, -1):
        if chance in charger:
            cnt += 1
            charge(chance)
            return cnt
    # 충전을 못했다면
    cnt = 0
    return cnt

# 주어진 입력만큼 반복
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))

    cnt = 0
    charge(0)
    print(f"#{tc} {cnt}")


