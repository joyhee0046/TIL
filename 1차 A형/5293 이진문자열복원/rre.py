import sys
sys.stdin = open("sample_input.txt", "r")

def binary_code(bin_list, cnt, ans_li):
    global check, ans, binary_list
    if cnt == check:
        ans = ans_li
        return ans

    for idx, bin in enumerate(bin_list):
        if bin == 0:  # 남은 수가 없으면 넘어가기
            continue
        if ans_li == []:
            ans_li.append(binary_list[idx][0])
            ans_li.append(binary_list[idx][1])
        elif idx == 0:  # A 00
            if ans_li[-1] == 1:
                continue
            ans_li.append(0)
        elif idx == 1:  # B 01
            if ans_li[-1] == 1:
                continue
            ans_li.append(1)
        elif idx == 2:  # C 10
            if ans_li[-1] == 0:
                continue
            ans_li.append(0)
        elif idx == 3:  # D 11
            if ans_li[-1] == 0:
                continue
            ans_li.append(1)

        bin_list[idx] -= 1
        cnt += 1
        binary_code(bin_list, cnt, ans_li)
        if ans != '':
            return ans
        cnt -= 1
        bin_list[idx] += 1
        ans_li.pop()
        if cnt == 0:
            ans_li.pop()

def binary_0(bin_list, cnt, ans_li):  #A나 B, 앞이 0으로 끝났을 때
    global check, ans, binary_list
    if cnt == check:
        ans = ans_li
        return ans
    for idx, bin in enumerate(bin_list):
        if bin == 0:  # 남은 수가 없으면 넘어가기
            continue
        if ans_li == []:
            ans_li.append(binary_list[idx][0])
            ans_li.append(binary_list[idx][1])
        elif idx == 0:  # A 00
            if ans_li[-1] == 1:
                continue
            ans_li.append(0)
        elif idx == 1:  # B 01
            if ans_li[-1] == 1:
                continue
            ans_li.append(1)

        bin_list[idx] -= 1
        cnt += 1
        sum(bin_list[0,1]
        binary_code(bin_list, cnt, ans_li)
        if ans != '':
            return ans
        cnt -= 1
        bin_list[idx] += 1
        ans_li.pop()
        if cnt == 0:
            ans_li.pop()


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

