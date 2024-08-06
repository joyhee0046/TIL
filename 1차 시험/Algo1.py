# import sys
# sys.stdin = open("algo1_sample_in.txt", "r")
# 캠퍼스 유지보수
# 유지 보수 비용과 해당 비용의 깊이를 곱하면 건물의 총 유지 보수 비용이 된다.
# 주어진 모든 건물의 총 비용의 합을 계산하라.

import json
T = int(input())  # 테스트케이스 수 입력받기
for tc in range(1, T+1):  # 테스트케이스만큼 반복
    N = int(input())  # 요소수 입력받기
    cost_li = json.loads(input().strip())  # 요소에 대한 비용 리스트 입력받기
    ans = 0  # 총 비용을 저장할 변수
    depth = 1  # 리스트 안에 있는 비용과 곱해줄 깊이

    def check_li(cost_li):  # 리스트 확인하며 계산할 함수
        global ans, depth  # 비용변수와 깊이변수
        for i in range(len(cost_li)):  # 리스트길이 확인하여 끝까지 반복
            if isinstance(cost_li[i], int):  # 해당 값이 정수인지 확인
                ans += cost_li[i]*depth  # 정수라면 깊이와 곱해서 총비용에 더하기
            else:
                depth += 1  # 정수가 아니라면 중첩리스트이므로 깊이 +1
                check_li(cost_li[i])  # 해당 중첩리스트를 다시 확인_재귀
        depth -= 1  # 리스트를 돌고 나왔으면 깊이 -1
        return  # 끝까지 돌았으면 함수 빠져나오기

    check_li(cost_li)  # 받은 리스트로 함수 실행시키기

    print(f"#{tc} {ans}")  # 케이스번호와 총비용 출력

    # C:\python3\pypy3.7-v7.3.4-win64\pypy3.exe C:/Users/test/Algo1.py
    # #1 13
    # #2 23
    # #3 0
    #
    # Process finished with exit code 0