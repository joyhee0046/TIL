import sys
sys.stdin = open("sample_input.txt", "r")

import string
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    li = []
    for _ in range(N):
        li.append(set(input()))
    # print(li)
    
    dict = {}
    dict[i in string.ascii_lowercase] = 0

    # for i in range(N):
    #     for j in range(li[i]):
    #         dict[li[i][j]] 
            
    print(dict)