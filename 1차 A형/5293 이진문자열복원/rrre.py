import sys
sys.stdin = open("sample_input.txt", "r")





binary_list = [[0, 0], [0, 1], [1, 0], [1, 1]]
T = int(input())
for tc in range(1, T + 1):
    bin_list = list(map(int, input().split()))

    ans_li = []
    check = sum(bin_list)
    ans = ''
    binary_code(bin_list, 0, ans_li)
    if ans == "":
        ans = "impossible"

    print(f"#{tc} ", *ans, sep="")

    keys = ["00", "01", "10", "11"]