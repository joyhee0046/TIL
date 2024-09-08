# import sys
# sys.stdin = open('sample_input.txt', 'r')

def dfs():
    # N개의 퀸을 모두 놓았다.
    if len(rdt) == N:
        global answer
        # 경우의 수 +1
        answer += 1
        return
    # N개의 퀸 놓기
    for i in range(N):
        # 퀸 놓을 수 있는지 확인하는 함수
        if isSvb(i):
            # i자리에 퀸 놓기
            rdt.append(i)
            # 다음 퀸 놓으러 가기
            dfs()
            # 원복
            rdt.pop()
    return

# 퀸 놓을 수 있는지 확인
def isSvb(cand):
    for row, col in enumerate(rdt):
        # 자리가 이미 차있거나, 다른 퀸을 공격할 수 있는 경우
        if cand == col or len(rdt) - row == abs(cand - col):
            # 퀸을 놓을 수 없음.
            return False
    # 퀸을 놓을 수 있음.
    return True

# 주어진 입력 받기
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    # 퀸 놓을 리스트 만들기
    rdt = []
    # 경우의 수 저장할 정답 변수 만들기
    answer = 0
    # 메인 함수 실행
    dfs()
    # 정답 출력
    print(f"#{tc} {answer}")