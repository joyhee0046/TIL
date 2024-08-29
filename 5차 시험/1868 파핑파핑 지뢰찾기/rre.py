import sys
sys.stdin = open('input.txt', 'r')



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    borad = [list(input()) for i in range(N)]