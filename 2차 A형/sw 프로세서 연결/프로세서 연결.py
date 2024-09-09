import sys
sys.stdin = open('sample_input (2).txt', 'r')
T = int(input())

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_wire_len_sum = float('INF')  # 연결한 전선의 길이의 합 ( 최소값 )
    max_connect_cnt = 0  # 최대로 연결한 프로세서의 개수 ( 최대값 )

    # 모서리에 있는 코어들은 선택할 필요가 아예 없다..
    # => 모서리에 있는 코어들은 이미 연결이 되어 있음

    core_list = []
    # 0 => 빈 칸, 1 => 프로세서
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            # 해당 좌표가 프로세서라면
            if arr[i][j]:
                core_list.append((i, j))
    def dfs(idx, connect_cnt, wire_len):
        """
        :param idx: 선택하려는 코어의 인덱스
        :param connect_cnt: 여태까지 선택한 코어의 개수
        :param wire_len: 설치한 전선의 길이의 합
        :return:
        """
        global max_connect_cnt, min_wire_len_sum

        # 현재까지 연결된 코어의 개수(connect_cnt) +
        # 남은 코어의 개수(전체 코어의 개수(core_list) - 현재 선택해야하는 코어(idx))가
        # 최대 코어의 개수보다 적으면 굳이 진행 x
        # 남은 개수를 다 선택해도 어차피 최대 코어의 개수를 못넘기면 => 굳이 할 필요가 없다 .
        if connect_cnt + (len(core_list) - idx) < max_connect_cnt:
            return

        # 모든 코어를 선택한 경우
        if idx == len(core_list):
            # 1. 연결된 코어의 수가 기존 최대로 선택한 코어의 수보다 크거나
            # 2. 연결된 코어의 수가 최대 코어랑 같으면 => 연결된 길이가 작으면 갱신
            if (connect_cnt > max_connect_cnt
                    or connect_cnt == max_connect_cnt and wire_len < min_wire_len_sum):
                max_connect_cnt = max(max_connect_cnt, connect_cnt)
                min_wire_len_sum = min(min_wire_len_sum, wire_len)

        # 해당 코어를 선택하지 않는 경우
        dfs(idx + 1, connect_cnt, wire_len)

        # 해당 코어를 선택한 경우
        # 선택한 코어의 좌표를 가지고 온다.
        cx, cy = core_list[idx]
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy  # 다음에 이동할 좌표
            # 이동할때마다 전선을 설치할 거다. (이동하는 좌표에 )
            # dfs 빠져나올 때, 뭘 해야한다? => 복구를 해야한다.
            # 전선을 설치했던 좌표를 저장할 임시 변수를 하나 만들어서, 거기에 전선 좌표를 저장해야한다.
            tmp_connect_pos_list = []

            # 벽 or 코어 or 전선을 만날 때까지 전선을 이어준다.
            while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                # 전선을 설치하고, 이동하는 로직을 작성을 한다.
                # 전선을 설치하는 좌표를 임시 공간에 저장한다.
                tmp_connect_pos_list.append((nx, ny))
                nx, ny = nx + dx, ny + dy

            # 벽까지 도달을 못했고 중간에 코어 or 전선을 부딪쳤다 ?
            # 이 경우에는 굳이 dfs를 진행할 필요가 없다.
            # 범위를 벗어났다는 건, 안 부딪치고 무사히 벽에 도달했다는 소리에요
            # 근데 만약에 아직도 범위안에 있다? 그러면 장애물 어딘가에 부딪쳐서 범위내에 있는거다
            if 0 <= nx < N and 0 <= ny < N:
                continue

            # 원본에 전선을 설치해준다.
            # -1 아니고, 자유롭게 해도됩니다. ( 0이랑 1만 아니면 됩니다 )
            for tx, ty in tmp_connect_pos_list:
                arr[tx][ty] = -1

            # 선택한 코어 개수 +1, 연결한 전선의 개수 + ,
            dfs(idx + 1, connect_cnt + 1, wire_len + len(tmp_connect_pos_list))

            # 원복
            for tx, ty in tmp_connect_pos_list:
                arr[tx][ty] = 0


    """
    파라미터
    1. 재귀를 종료할 파라미터 => 선택해야 하는 코어의 IDX  = 코어의 개수에 도달하면 종료 
    2. 누적해서 가져가고 싶은 값
    => 선택한 프로세서의 개수(최대 개수를 구하려고 하니까), 선택한 프로세서들의 전선의 길이 합 ( 최소 길이 )
    """
    dfs(0, 0, 0)
    print(f"#{test_case} {min_wire_len_sum}")
