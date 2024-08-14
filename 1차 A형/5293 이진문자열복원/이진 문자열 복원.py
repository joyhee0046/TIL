import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    result = ''
    binary_cnt_list = list(map(int, input().split()))
    binary_types = ['00', '01', '10', '11']


    def dfs(string, cnt_list):
        global result

        # 이미 결과를 찾은 경우에는 함수를 바로 종료
        if result:
            return

        # 01 이 나온다면, 반드시 다음에 10이 나와야한다.
        # 만약에 01 다음에 11 이 나온다면, 결국 11 다음에는 11이나 10 이 나온다
        # 결국 01 이 나오면, 뒤에 뭐가 됐든 10이 나오기 전에는 01이 나올 수 없다 .
        # 그렇기 때문에 01과 10의 개수 차이는 2개 이상이 될 수 없다.
        if abs(cnt_list[1] - cnt_list[2]) > 1:
            return

        # 모든 문자를 다 사용해서, 결과를 찾은 경우
        if sum(cnt_list) == 0:
            result = string
            return

        # 마지막 문자가 0 으로 끝나는 경우에 반드시 "00" or "01" 로 시작해야하므로
        # 해당 문자의 가용개수가 남아있다면,
        # 00인 경우에는 기존 문자열에 "0" 을 추가하고,
        # "00" 개수를 나타내는 index 개수를 하나 줄여서 다음 dfs로 전달
        # 위와 같은 과정으로
        # 0 으로 끝나고, (00, 01) 로 이어서 시작하는 케이스
        # 1로 끝나고, (10, 11) 로 이어서 시작하는 케이스를 반복해서 호출한다.
        if string[-1] == '0':
            if cnt_list[0] > 0:
                cnt_list[0] -= 1
                dfs(string + '0', cnt_list)
                cnt_list[0] += 1

            if cnt_list[1] > 0:
                cnt_list[1] -= 1
                dfs(string + '1', cnt_list)
                cnt_list[1] += 1

        if string[-1] == '1':
            if cnt_list[2] > 0:
                cnt_list[2] -= 1
                dfs(string + '0', cnt_list)
                cnt_list[2] += 1

            if cnt_list[3] > 0:
                cnt_list[3] -= 1
                dfs(string + '1', cnt_list)
                cnt_list[3] += 1

    # 주어진 00, 01, 10, 11 4개의 문자열로 시작하는 케이스에 대해서 모두 DFS를 실행
    for idx in range(len(binary_types)):
        # 패턴이 존재하는 경우에만 시작
        if binary_cnt_list[idx] > 0:
            # 해당 문자열로 시작하는 경우, 개수를 차감하고 dfs 함수를 실행함
            binary_cnt_list[idx] -= 1

            # 각 루프에 맞는 시작 문자열과 남은 문자열 개수 리스트를 파라미터로 건넴
            dfs(binary_types[idx], binary_cnt_list)

            # 다음 DFS 실행할 때, 기존 변경사항이 영향을 주지 않도록 원복
            binary_cnt_list[idx] += 1

        # 이미 결과를 도출했다면 for loop 중단
        if result:
            break

    print(f"#{test_case} {result or 'impossible'}")
