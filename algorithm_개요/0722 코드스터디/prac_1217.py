import sys

def exp (i,n):
    if n == 1:
        return i
    else:
        return i * exp(i,n-1)

sys.stdin = open("input_1217.txt",'r')

for test_case in range(1,11):
    num = int(input())
    n,m = map(int,input().split())
    ans = exp(n,m)
    print(f'#{test_case} {ans}')