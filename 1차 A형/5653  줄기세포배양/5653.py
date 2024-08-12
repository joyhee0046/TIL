# 2차월 배열 2개
# 원본에서 시간 확인
# 체크에서 default:활성/비활성 체크 , 남은 시간 체크
# 활성 끝나서 비활성 된,죽은 세포는 0으로 바꾸기
# 한 칸에 중복되면 max로 처리

## t_tip : 생성된 후의 시간을 저장해서 시간이 더 많이 지났으면 pass로 처리할수도 있음.
## 2차원 평면이 계속 확장되기 위해서 좌표값을 키로 하는 딕셔너리 형식으로 관리.

import sys
sys.stdin = open("sample_input.txt", "r")

def check_stem_cell(list, tt_time):
    pass

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    check = li[:]

    check_stem_cell(check, K)

    ans = 0
    for i in range(len(check)):
        if check[i] > 0:
            ans += 1
