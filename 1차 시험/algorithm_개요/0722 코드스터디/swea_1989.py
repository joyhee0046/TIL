def check_palindrome(txt, index):
    # 더 이상 비교할 친구가 없으면 True를 던지고 탈출
    if index >= len(txt) / 2:
        return True
    # 문자가 불일치하면 False를 던지고 탈출
    elif txt[index] != txt[-index-1]:
        return False
    # 아니라면 둘 사이를 비교
    else:
        return check_palindrome(txt, index + 1)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    txt = input()
    if check_palindrome(txt, 0):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
