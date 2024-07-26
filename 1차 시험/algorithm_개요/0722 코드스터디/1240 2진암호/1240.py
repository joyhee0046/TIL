import sys
sys.stdin = open("input.txt", "r")

code = ['1011000', '1001100', '1100100', '1011110', '1100010',
        '1000110', '1111010', '1101110', '1110110', '1101000']

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    result = -1
    for i in range(n):
        line = input()
        if result == -1 :
            if int(line) != 0:
                line = str(int(line[::-1]))
                data = []
                for j in range(8):
                    data.append(code.index(line[j * 7:j * 7 + 7]))

                solve = (data[1] + data[3] + data[5] + data[7]) * 3 + data[0] + data[2] + data[4] + data[6]

                if solve % 10 == 0:
                    result = sum(data)
                else:
                    result = 0
    print(f"#{tc} {result}")