import sys

sys.stdin = open("input_1240.txt",'r')

T = int(input())

password_num = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]

for test_case in range(1,T+1):
    N , M = map(int,input().split())
    lines = [list(map(int,input().rstrip())) for _ in range(N)]
    for line in lines:
        if sum(line) == 0:
            continue
        reverse_line = list(reversed(line))
        idx = reverse_line.index(1)
        password_line = reverse_line[idx:idx+56]
        password_line.reverse()
        break

    passwords = []
    for i in range(8):
        password = password_line[i*7:(i+1)*7]
        passwords.append(password_num.index(password))

    check = 0
    for idx,val in enumerate(passwords):
        if idx % 2 == 0:
            check += val * 3
        else:
            check += val

    if check % 10 ==0 :
        ans = sum(passwords)
        print(f'#{test_case} {ans}')
    else:
        print(f'#{test_case} 0')
