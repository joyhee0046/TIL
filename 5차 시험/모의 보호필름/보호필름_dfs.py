def inspect():
    for w in range(W):
        k_sum = 1
        for j in range(D - 1):
            # 다음 셀이랑 비교해서 일치하면 +1, 다르면 초기화
            if matrix[j][w] == matrix[j + 1][w]:
                k_sum += 1
            else:
                k_sum = 1
            # 기준치를 만족시키면 중단
            if k_sum == K:
                break
        else:  # for 문이 끝까지 돌았다는 건 없다는 것
            return False
    return True

# remain_cnt : 남은 투입 횟수
# start_idx : 다음 투입을 어디서부터 시작할건지
def dfs(remain_cnt, start_idx):
    # 남은 투입횟수가 0 이되면 검사
    # 투입횟수 횟수로 바꿔도 됩니다.
    if remain_cnt == 0:
        return inspect()

    """
    현재 집어넣은 위치 이전에는 제외하고 투입을 한다. 
    그 다음부터 투입을 하면 된다. 
    dfs 가 진행될 수록 투입 시작 위치는 +1 이 되고, 그 위치부터 다시 투입을 시작하기 때문에
    자연스럽게 이전 영역은 투입하지 않는다 => 조합 
    """
    for s in range(start_idx, D):
        # s : 선택한 행의 인덱스
        tmp_arr = matrix[s]
        matrix[s] = [0] * W
        if dfs(remain_cnt - 1, start_idx + 1):
            return True
        matrix[s] = [1] * W
        if dfs(remain_cnt - 1, start_idx + 1):
            return True
        matrix[s] = tmp_arr
    return False

# 주어진 입력 받기
T = int(input())
for tc in range(1, T + 1):
    # D: 보호필름 두께, W: 가로크기, K: 합격기준
    D, W, K = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(D)]
    min_inject_cnt = 0
    # 두께만큼 약품 투입 가능
    for inject_cnt in range(D + 1):
        if dfs(inject_cnt, 0):  # 남은 투입 횟수, 인덱스. 첫줄부터 돌려보기
            min_inject_cnt = inject_cnt  # 갱신
            break
    print(f"#{tc} {min_inject_cnt}")