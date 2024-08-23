import sys
sys.stdin = open("sample_input.txt", 'r')

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))

    # 버블정렬을 끝까지 몇 번 돌지
    for j in range(N-1):
        # 한 바퀴에 버블을 몇 번 확인해야 하는지_매 시행마다 마지막 한자리가 확정되므로 확인할 범위가 점점 줄어들어야 함.
        for i in range(N-1-j):
            # 대소관계 확인
            if li[i] > li[i+1]:
                # 위치에 맞게 바꿔주기
                temp = li[i]
                li[i] = li[i+1]
                li[i+1] = temp

    # 가장 큰 수와 가장 작은 수의 차이
    ans = li[-1] - li[0]

    # 출력
    print(f"#{tc} {ans}")