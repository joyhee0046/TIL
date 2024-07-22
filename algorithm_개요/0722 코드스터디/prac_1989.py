import sys
sys.stdin = open("input_1989.txt",'r')

T = int(input())

def palindrome(input_string):
    if len(input_string) <= 1:
        return 1
    front = input_string.pop(0)
    end = input_string.pop()
    if front == end:
        return palindrome(input_string)
    else:
        return 0

for test_case in range(1,T+1):
    input_string = list(map(str,input().rstrip()))
    ans = palindrome(input_string)
    print(f'#{test_case} {ans}')