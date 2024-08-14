import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1,1+T):
    M, A = map(int,input().split())
    Ali = list(map(int,input().split()))
    Bli = list(map(int,input().split()))
    AP = []
    for _ in range(N):
        AP.append(list(map(int,input().split())))

