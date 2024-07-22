num = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, 
       '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    start, end = -1, -1
    cipher_code = []

    # 한 줄씩 읽어서 암호코드가 있는 한 줄만 얻어낸다
    for _ in range(N):
        arr = list(map(int, input()))
        if 1 in arr:
            for j in range(M - 1, 0, -1):
                if arr[j] == 1:
                    cipher_code = arr[j - 55:j + 1]
                    break

    # 암호코드를 원래 숫자로 해독한다
    plain_code = []
    for i in range(8):
        temp_code = ''
        for j in range(7 * i, 7 * i + 7):
            temp_code += str(cipher_code[j])
        if temp_code in num:
            plain_code.append(num[temp_code])

    # 해독된 숫자를 검증한다
    # (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수
    temp = 0
    for i in range(len(plain_code)):
        if i % 2 == 0:
            temp += plain_code[i] * 3
        else:
            temp += plain_code[i]

    if temp % 10 != 0:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {sum(plain_code)}')
