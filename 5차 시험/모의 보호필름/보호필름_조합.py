from itertools import combinations

# 성능검사하는 함수
def inspect():
    # 모든 열에 대해서 검사
    for w in range(W):
        # 시작셀의 연속된 특성은 1부터 카운트 시작
        k_sum = 1
        # 하나의 열을 검사 ! => 우리는 모든 열을 검사해야 한다.
        for j in range(D - 1):
            # 바로 아랫 행과 같은 특성인 지 비교
            if matrix[j][w] == matrix[j + 1][w]:
                k_sum += 1
            else:
                k_sum = 1
            # 검사하는 도중에 K에 도달하면, 중단
            if k_sum == K:
                break
        # 위의 내부 for문을 끝까지 돈다 ? => 성능 K에 도달하지 못했다.
        else:
            return False
    # 모든 열에 대해서 검사 통과했다는 소리
    return True

# depth: 약품 투입 횟수
# depth = 0 => 첫 번째로 투입할 막을 선택하는 idx
def dfs(depth):
    # 종료하는 조건
    if depth == len(selected_layers):
        return inspect()  # 검사해서 성공하면 True
    # D=4 => range(D) => [0, 1, 2, 3] => combination 3개를 선택한다고 그러면
    # [0, 1, 2], [0, 1, 3], [0, 3]
    # 맨 처음 조건을 주어진 matrix에 접근
    layer_depth = selected_layers[depth]
    tmp_arr = matrix[layer_depth]

    # 바꿀 레이어 선택해서 작업
    matrix[layer_depth] = [0] * W
    if dfs(depth + 1):
        return True

    matrix[layer_depth] = [1] * W
    if dfs(depth + 1):
        return True

    matrix[layer_depth] = tmp_arr

    # 위의 dfs 함수에서 True를 한 번도 경험하지 못한 경우
    return False


T = int(input())
for test_case in range(1, 2):
    # 두께, 셀의 개수, 합격 기준
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]
    min_inject_cnt = -1  # 최소 약품 투입 횟수

    # 약품 투입횟수를 0부터 D 번까지 늘려나가면서 테스트할 거다.
    for inject_cnt in range(D+1):
        # 투입을 안한다 그러면, 바로 검사하면 된다.
        if inject_cnt == 0:
            # 주어진 셀들을 검사하는 함수
            # 검사가 성공하면 True
            if inspect():
                min_inject_cnt = 0
                break

        # 두께 D 까지가 있으면
        print("Range: ", range(D), inject_cnt)
        for selected_layers in combinations(range(D), inject_cnt):

            # 우리가 조합적으로 선택한 레이어에 약품을 투입한 경우가
            # 성공적으로 성능검사를 통과한다면, 최소 약품 투입횟수를 갱신하고, 종료
            # DFS
            # 파라미터
            # 1. 재귀호출을 종료할 파라미터
            # 우리가 선택한 레이어의 개수 ( selected_layers 개수 = inject_cnt )
            # 여태까지 약품을 투입한 횟수 (초기값은 0 , depth )
            # 2. 누적해서 가져가고 싶은 값 => 정답값은 걸 넣었어요. (일단은 지금 없어도 될 것 같다 )
            if dfs(0):
                min_inject_cnt = inject_cnt
                break

    print(f"#{test_case} {min_inject_cnt}")