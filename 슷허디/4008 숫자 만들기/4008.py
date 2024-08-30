import sys
sys.stdin = open('sample_input (1).txt', 'r')

# 주어진 입력 받기
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    oper_li = list(map(int, input().split()))
    num_li = list(map(int, input().split()))

    # +자리부터 차례로 넣뺏해서 끝까지 계산하는 모음 만들기..
