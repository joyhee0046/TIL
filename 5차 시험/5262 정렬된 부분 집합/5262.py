import sys
sys.stdin = open('sample_input(2).txt', 'r')

def find_ans(nums):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

T = int(input())
for tc in range(1, T+1):
    li = list(map(int, input().split()))
    n = li[0]
    nums = li[1:]

    print(f"#{tc} {find_ans(nums)}")