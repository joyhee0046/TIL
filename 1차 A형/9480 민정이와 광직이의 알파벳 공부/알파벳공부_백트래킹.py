import sys
sys.stdin = open('sample_input.txt')


# 입력 처리 및 결과 출력
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    words = [input().strip() for _ in range(N)]
    # 글자 내에서 중첩되는 글자 수를 줄인다.
    word_sets = [set(word) for word in words]
    # word_sets = [set(input().strip()) for _ in range(N)]
    word_set_cnt = 0


    def dfs(depth, current_set):
        global word_set_cnt

        if depth == len(word_sets):
            if len(current_set) == 26:
                word_set_cnt += 1
            return

        # 현재 단어를 선택하는 경우
        # | 는 파이썬 set 의 합집합
        dfs(depth + 1, current_set | word_sets[depth])

        # 현재 단어를 선택하지 않는 경우
        dfs(depth + 1, current_set)

    dfs(0, set())

    print(f"#{t} {word_set_cnt}")
