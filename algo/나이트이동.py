import sys
sys.stdin = open('7562.txt', 'r')

T = int(input())
for tc in range(T):
    i = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    borad = list([0] * i for _ in range(i))

    