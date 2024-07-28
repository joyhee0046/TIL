#조합 순열 마스터 함수
def iterator_fc(arr, n):
    result = []  # 결과를 저장할 리스트
    if n == 1:
        return [[i] for i in arr]
    for i in range(len(arr)):
        elem = arr[i]
        # for rest in iterator_fc(arr[i + 1:], n - 1):  # 조합
        # for rest in iterator_fc(arr[:i] + arr[i+1:], n - 1):  # 순열
        # for rest in iterator_fc(arr, n - 1):  # 중복순열
        # for rest in iterator_fc(arr[i:], n - 1):  # 중복조합
            result.append([elem] + rest)
    return result
print(iterator_fc([1, 2, 3, 4], 3))

# 팩토리얼 계산
def fact(n):
    # Basis Rule: n이 1 이하인 경우 1을 반환합니다.
    if n <= 1: return 1
    # Inductive Rule: (n-1)로 자기 자신을 호출하는 재귀 케이스
    else: return n * fact(n - 1)
print(fact(5))  # 5*4*3*2*1을 계산하여 120 출력

# 피보나치 수열
def fibonacci(n):
    # 기본 규칙: n이 0일 때, 0을 반환합니다.
    if n == 0: return 0
    # 기본 규칙: n이 1일 때, 1을 반환합니다.
    elif n == 1: return 1
    # 귀납 규칙: n이 2 이상일 때, F(n-1) + F(n-2)를 반환합니다.
    else: return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10)) # 55 (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55_재귀로 10까지 계산)

# 피보나치 수열 메모이제이션
def fibo1(n):
    global memo  # 전역 변수 memo 선언
    # n이 2 이상이고 memo[n]이 아직 계산되지 않아서 0이라면
    if n >= 2 and memo[n] == 0:
        # memo[n]에 fibo1(n-1)과 fibo1(n-2)의 합을 저장하여 재귀적으로 피보나치 수 계산
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n] #현재 n에 대한 피보나치 수
num = 10
memo = [0] * (num+1)  # n+1 크기의 리스트를 생성하고 모든 값을 0으로 초기화
memo[0] = 0  # 피보나치 수열의 첫 번째 수는 0
memo[1] = 1  # 피보나치 수열의 두 번째 수는 1
print(f"피보나치 수열의 {num}번째 수는 {fibo1(num)}")  # 결과 출력

# 순열 반복문
for i in range(1, 4):  # i는 1에서 3까지의 값을 가지고, 첫 번째 자리의 숫자를 의미
    for j in range(1, 4):  # j는 1에서 3까지의 값을 가지고, 두 번째 자리의 숫자를 의미
        if j != i:  # j가 i와 같지 않은 경우에만 다음 블록을 실행
            for k in range(1, 4):  # k는 1에서 3까지의 값을 가지고, 세 번째 자리의 숫자를 의미
                if k != i and k != j:  # k가 i와 j와 같지 않은 경우에만 다음 블록을 실행
                    print(i, j, k)  # 서로 다른 세 숫자의 순열을 의미

# 순열 함수
def perm(selected, remain):
    if not remain:  # 남은 요소들이 없는 경우
        print(selected)  # 선택된 요소들 출력
    else:  # 남은 요소들이 있는 경우
        for i in range(len(remain)):  # 남은 요소들의 인덱스 순회
            select_i = remain[i]  # 현재 인덱스 i에 해당하는 요소 선택
            remain_list = remain[:i] + remain[i+1:]  # 선택된 요소를 제외한 새로운 남은 요소 리스트 생성
            perm(selected + [select_i], remain_list)  # 선택된 요소를 추가한 리스트와 새로운 남은 요소 리스트로 재귀 호출
perm([], [1, 2, 3])

# 조합 반복문
for i in range(1, 5):  # 1~4중 첫선택
    for j in range(i+1, 5):  # 첫선택 제외하고 두번째선택
        for k in range(j+1, 5):  # 2선택까지 제외하고 3선택
            print(i, j, k)  # 다른 세 숫자의 조합

# 조합 함수
def comb(arr, n):  #arr 배열에서 n개의 요소를 선택
    result = []  # 결과를 저장할 리스트
    if n == 1:  # 선택할 요소의 수가 1인 경우, 각 요소를 리스트로 감싸서 반환
        return [[i] for i in arr]
    for i in range(len(arr)):    # 배열의 각 요소에 대해 반복
        elem = arr[i]  # 현재 요소를 선택
        # 현재 요소 이후의 나머지 요소들로 n-1개의 조합을 재귀적으로 생성
        for rest in comb(arr[i + 1:], n - 1):  # arr[i+1:]는 현재 요소 이후의 모든 요소를 포함
            result.append([elem] + rest)  # 현재 선택한 요소와 재귀 호출을 통해 얻은 조합을 합침
    return result  # 최종 조합 결과 반환
print(comb([1, 2, 3, 4], 3))  # [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4] 출력

# itertools 모듈 사용
import itertools
arr = [1, 2, 3]
# 순열
print(tuple(itertools.permutations(arr)))
# 조합
print(tuple(itertools.combinations(arr, 2)))
# 중복순열
print(tuple(itertools.product(arr, repeat=2)))
# 중복 조합
print(tuple(itertools.combinations_with_replacement(arr, 2)))

# 베이비진
def is_babygin(cards):
    counter = [0] * 10
    ans_condition = 0
    for card in cards:  # 어떤 수가 몇장있는지 세기
        counter[card] += 1
    for count in counter:  # 3장이상 같은 카드가 있는지 확인
        if count >= 3:
            ans_condition += 1
    for i in range(8):  # # 카드가 순서대로 놓였는 지 확인
        if counter[i] >= 1 and counter[i+1] >= 1 and counter[i+2] >= 1:
            ans_condition += 1
    if ans_condition == 2:
        return True
    return False
numbers_1 = [6, 6, 6, 7, 7, 7]
numbers_2 = [2, 3, 5, 7, 7, 7]
print(f"{numbers_1} 은 baby-gin이 {is_babygin(numbers_1)}")
print(f"{numbers_2} 은 baby-gin이 {is_babygin(numbers_2)}")

# 하노이탑
def hanoi(n, source, target, auxiliary): # 디스크수, 초기위치, 목표위치, 보조기둥
    if n > 0:
        # 1. n-1개의 디스크를 source에서 auxiliary로 이동 (재귀 호출)
        hanoi(n - 1, source, auxiliary, target)
        # 2. 하나의 디스크를 source에서 target으로 이동
        print(f"Move disk {n} from {source} to {target}")
        # 3. n-1개의 디스크를 auxiliary에서 target으로 이동 (재귀 호출)
        hanoi(n - 1, auxiliary, target, source)
hanoi(3, 'A', 'C', 'B')  # 'A'에서 'C'로 이동, 'B'는 보조

##########################

# 부분집합 반복문
selected = [0] * 3
for i in range(2):
    selected[0] = i  # 첫 번째 값 설정
    for j in range(2):
        selected[1] = j  # 두 번째 값 설정
        for m in range(2):
            selected[2] = m  # 세 번째 값 설정
            subset = []  # 부분 집합을 저장할 리스트
            for n in range(3):  # selected 리스트의 각 요소에 대해 반복
                if selected[n] == 1:  # 요소가 1인 경우
                    subset.append(n+1)  # 부분 집합에 요소 추가 (1부터 시작하도록 조정)
            print(subset)  # 현재 부분 집합 출력

# 부분집합 함수
def create_subset(depth, included):
    if depth == len(input_list):  # 재귀 호출 깊이가 input_list의 길이와 같아지면
        cnt_subset = [input_list[i] for i in range(len(input_list)) if included[i]]  # 포함된 요소들로 부분 집합 생성
        subsets.append(cnt_subset)  # 생성된 부분 집합을 subsets 리스트에 추가
        return
    included[depth] = False # 현재 요소를 포함하지 않는 경우
    create_subset(depth + 1, included)  # 다음 깊이로 재귀 호출
    included[depth] = True # 현재 요소를 포함하는 경우
    create_subset(depth + 1, included)  # 다음 깊이로 재귀 호출
input_list = [1, 2, 3]  # 부분 집합을 생성할 입력 리스트
subsets = []  # 모든 부분 집합을 저장할 리스트
init_included = [False] * len(input_list)  # 각 요소의 포함 여부를 저장할 리스트 초기화
create_subset(0, init_included)  # 부분 집합 생성 함수 호출
print(subsets)  # 생성된 모든 부분 집합 출력

# 스택 구조_LIFO_를 리스트와 함수로 만들기
class Stack:
    def __init__(self):
        self.stack = []  # 스택을 빈 리스트로 초기화
    def push(self, item):
        self.stack.append(item)  # 스택의 맨 끝에 아이템 추가
    def pop(self):
        if not self.is_empty():  # 스택이 비어 있지 않은 경우
            return self.stack.pop()  # 스택의 맨 끝 아이템 제거 및 반환
        else:
            print("스택이 비었습니다.")  # 스택이 비어 있는 경우 경고 메시지 출력
    def peek(self):
        if not self.is_empty():  # 스택이 비어 있지 않은 경우
            return self.stack[-1]  # 스택의 맨 끝(위) 아이템 반환
        else:
            print("스택이 비었습니다.")  # 스택이 비어 있는 경우 경고 메시지 출력
    def is_empty(self): # 스택이 비어 있는지 확인하는 메서드
        return len(self.stack) == 0

# 중위표기식을 후위표기식으로 변환
def infix_to_postfix(expression):
    # 연산자의 우선순위를 정의
    op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []  # 연산자를 저장할 스택
    postfix = []  # 후위 표기식을 저장할 리스트
    for ch in expression:
        if ch.isnumeric():  # 숫자인 경우
            postfix.append(ch)  # 후위 표기식에 추가
        elif ch == '(':  # 여는 괄호인 경우
            stack.append(ch)  # 스택에 추가
        elif ch == ')':  # 닫는 괄호인 경우
            top_token = stack.pop()  # 스택에서 연산자를 꺼냄
            while top_token != '(':  # 여는 괄호를 만날 때까지
                postfix.append(top_token)  # 후위 표기식에 추가
                top_token = stack.pop()
        else:  # 연산자인 경우
            # 스택에 들어 있는 연산자가 지금 검사하는 연산자보다 우선순위가 더 높은 경우
            # 높은 친구들을 모두 거내서 후위 표기식에 추가하고, 검사하는 연산자를 스택에 추가
            while stack and op_dict[stack[-1]] >= op_dict[ch]:
                postfix.append(stack.pop())
            stack.append(ch)
    while stack:  # 스택에 남아 있는 모든 연산자를 후위 표기식에 추가
        postfix.append(stack.pop())
    return ' '.join(postfix)  # 리스트를 문자열로 변환하여 반환

# 후위 표기식 계산 함수
def run_calculator(expr):
    stack = []  # 피연산자를 저장할 스택
    tokens = expr.split()  # 후위 표기식을 공백으로 구분하여 토큰으로 분리
    for token in tokens:
        if token.isnumeric():  # 숫자인 경우
            stack.append(int(token))  # 스택에 추가
        else:  # 연산자인 경우
            op2 = stack.pop()  # 스택에서 두 번째 피연산자를 꺼냄
            op1 = stack.pop()  # 스택에서 첫 번째 피연산자를 꺼냄
            if token == '+':
                result = op1 + op2
            elif token == '-':
                result = op1 - op2
            elif token == '*':
                result = op1 * op2
            elif token == '/':
                result = op1 / op2
            stack.append(result)  # 계산 결과를 스택에 추가
    return stack.pop()  # 최종 결과를 반환

# 큐를 활용한 마이쮸 문제
from collections import deque
total_candy = 20  # 총 마이쮸 개수
queue = deque()  # 사람들을 저장할 큐
queue.append((1, 1))  # 첫 번째 사람과 받을 마이쮸 개수를 큐에 추가
last_person = None  # 마지막으로 마이쮸를 받은 사람을 저장할 변수
person_cnt = 1  # 첫번째 사람부터 시작
while total_candy > 0:  # 마이쮸가 남아 있는 동안 반복
    person, count = queue.popleft()  # 큐에서 사람과 받을 마이쮸 개수를 꺼냄
    if total_candy - count <= 0:  # 남은 마이쮸가 현재 사람이 받을 마이쮸 개수보다 적거나 같은 경우
        last_person = person  # 마지막으로 마이쮸를 받은 사람으로 현재 사람을 설정
        break
    total_candy -= count  # 현재 사람이 받을 마이쮸 개수를 총 마이쮸 개수에서 뺌
    person_cnt += 1
    queue.append((person, count + 1))  # 현재 사람은 다음 차례에 받을 마이쮸 개수를 1 증가시켜 큐에 다시 추가
    queue.append((person_cnt, 1))  # 다음 사람을 큐에 추가, 받을 마이쮸 개수는 1로 설정
print(f"마지막 마이쮸는 {last_person}번")  # 마지막으로 마이쮸를 받은 사람을 출력

##########################

# 이진트리
class TreeNode:
    def __init__(self, key):
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드
        self.val = key  # 노드의 값
# 트리 생성
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# 부모-왼-오 순회
def preorder_traversal(root):
    if root:
        print(root.val)  # 현재 노드 방문
        preorder_traversal(root.left)  # 왼쪽 서브트리 방문
        preorder_traversal(root.right)  # 오른쪽 서브트리 방문
# 왼-부모-오 순회
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)  # 왼쪽 서브트리 방문
        print(root.val)  # 현재 노드 방문
        inorder_traversal(root.right)  # 오른쪽 서브트리 방문
# 왼-오-부모 순회
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)  # 왼쪽 서브트리 방문
        postorder_traversal(root.right)  # 오른쪽 서브트리 방문
        print(root.val)  # 현재 노드 방문

# 이진트리 리스트로 만들고 중위순회
def in_order(node) :
    if node :
        in_order(data[node][2]) #left
        print(data[node][1], end="")
        in_order(data[node][3]) #right
for tc in range(1,11):
    N = int(input())
    data = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    for arr in data :
        while len(arr) != 4:
            arr.append(0)
    data.insert(0, [0,0,0,0])
    in_order(1)
    print()

# 이진트리 리스트로 만들고 중위순회_인덱스로 찾아가기
def tree_search(node_num, value, left=None, right=None):
    result = ''
    # 자식 노드가 있다면
    # if len(tree_dict[node_num]) == 3:
    if left:
        # 왼쪽 노드
        result += tree_search(node_num * 2, *tree_dict[node_num * 2])
        # 현재 노드
        result += value[0]
        if right:
            # 오른쪽 노드
            result += tree_search(node_num * 2 + 1, *tree_dict[node_num * 2 + 1])
    # 자식 노드가 없다면
    else:
        result += value[0]
    return result
for t in range(10):
    n = int(input())
    tree_dict = {i: input().split()[1:] for i in range(1, n + 1)}
    result = tree_search(1, *tree_dict[1])
    print(f"#{t + 1} {result}")

##############################

# 목표지점찾아가기(사다리)
dxy = [[1, 0], [0, -1], [0, 1]] # 아래, 좌, 우
def search_leader(x, y):
    # 원본을 훼손하지 않고, 방문체크할 수 있는 변수를 생성
    visited = [[0] * 100 for _ in range(100)]
    visited[x][y] = 1
    # 맨 밑에 도달할 때까지 반복
    while x != 99:
        # 3방향으로 움직이는거 ( 아래, 좌, 우)
        for dx, dy in dxy:
            # 방향에 따라서 다음에 움직일 좌표를 구함
            nx = x + dx
            ny = y + dy
            # 범위를 벗어난 경우에는 이건 옳지 않은 케이스
            if nx < 0 or nx >= 100 or ny <0 or ny >= 100:
                continue
            # 길이 아닌 경우
            if not data[nx][ny]:
                continue
            # 이미 방문한 경우
            if visited[nx][ny]:
                continue
            visited[x][y] = 1
            x, y = nx, ny
    # 마지막에 도달하고, 목적지가 2인 경우 (최종 목적지)
    if data[x][y] == 2:
        return True
    return False
for _ in range(1, 11):
    tc = int(input())
    result = -1  # 찾지 못하면 -1
    data = [list(map(int, input().split())) for _ in range(100)]
    # 출발점부터 시작을 해야 한다.
    # 출발점은 0행에 있고, 1인 부분을 찾자
    for j in range(100):
        if data[0][j] == 0:
            continue
        # 출발점이라는 소리
        if search_leader(0, j):
            result = j
            break
    print(f"#{tc} {result}")

# 장훈이 키 비트연산
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    res = float('inf')
    def get_subsets_bitmask():  #부분집합을 비트마스크로 구현하는 코드
        global res
        subset_cnt = 2 ** N
        # 모든 경우의 수
        for i in range(1, subset_cnt):  # i 에 해당하는 숫자들을 비트로 바꿔서 비트연산을
            h_sum = 0
            for j in range(N):
                if i & (1 << j):
                    h_sum += arr[j]
            if h_sum >= B:
                res = min(res, h_sum)
        return
    get_subsets_bitmask()
    print(f'#{tc} {res - B}')

# 장훈이 키 DFS
T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())  #사람수, 목표높이
    arr = list(map(int, input().split()))
    res = 10000 * N  # 절대 넘지않을 최대값
    def dfs(idx, h_sum): # 탐색중인 인덱스, 계산된 키
        global res
        if h_sum >= res:
            return
        if idx == N: # 현재 키의 합이 목표 높이 이상이면, 최소값 갱신
            if h_sum >= B:
                res = min (res, h_sum)
            return
        dfs(idx + 1, h_sum + arr[idx])  # 현재 idx가 가리키는 직원의 키를 포함하는 경우
        dfs(idx + 1, h_sum)  # 현재 idx가 가리키는 직원의 키를 포함하지 않는 경우
    dfs(0, 0)
    print(f"#{test_case} {res - B}")

# 숫자카드랑 사칙연산카드로 숫자만들기 DFS
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    op_input_list = list(map(int, input().split()))
    number_list = list(map(int, input().split()))
    max_num = -100000000
    min_num = 100000000
    def create_num(op_list, idx, res):
        global max_num, min_num
        # 모든 숫자를 다 계산했다면
        if idx == N:
            max_num = max(max_num, res)  # 최대값 갱신
            min_num = min(min_num, res)  # 최소값 갱신
            return
        # 남은 연산자에 대해서 하나씩 시도
        # 0 => '+', 1 => '-', 2 => '*', 3 => '/'
        for op_idx, op_cnt in enumerate(op_list):
            if op_cnt == 0:  # 남은 연산자가 없으면 해당 연산자는 skip
                continue
            tmp_res = res
            if op_idx == 0:  # +
                tmp_res += number_list[idx]
            elif op_idx == 1:  # -
                tmp_res -= number_list[idx]
            elif op_idx == 2:  # *
                tmp_res *= number_list[idx]
            elif op_idx == 3:  # /
                if number_list[idx] == 0:  # 분모가 0인 경우는 계산 X
                    return
                # ( -2 / 3 = 0이 나와야 함 )
                tmp_res = int(tmp_res / number_list[idx])
            else:
                print("주어진 입력이 아닙니다 ~~~~ ")
            op_list[op_idx] -= 1
            create_num(op_list, idx + 1, tmp_res)
            op_list[op_idx] += 1
    init_num = number_list[0]
    init_idx = 1
    create_num(op_input_list, init_idx, init_num)
    print(f"#{test_case} {max_num - min_num}")

# 미로찾기 DFS
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for _ in range(10):
    MAZE_SIZE = 16
    START_POS = (1, 1)
    END_POS = (13, 13)
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(MAZE_SIZE)]
    visited = [[False] * MAZE_SIZE for _ in range(MAZE_SIZE)]
    result = 0
    def dfs(x, y):
        global result
        # 목적지에 도착하면 결과를 1로 바꾼 후에 리턴
        if (x, y) == END_POS:
            result = 1
            return
        # 이미 결과가 나온 경우에는 이후의 dfs를 진행하지 않음
        if result == 1: return
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= MAZE_SIZE or ny < 0 or ny >= MAZE_SIZE: continue
            if visited[nx][ny]: continue
            if maze[nx][ny] == 1: continue
            visited[nx][ny] = True
            dfs(nx, ny)
        return
    # 파라미터를 뭘로 할까요 ?
    # 1. 종료 조건을 위한 파라미터 ( 위치 정보 )
    # 2. 누적되는 결과값 파라미터 ( 딱히 필요없을 거 같아요 )
    dfs(*START_POS)  # 언패킹(Asterisk)
    print(f'#{tc} {result}')

# 미로찾기 BFS
from collections import deque
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for _ in range(10):
    MAZE_SIZE = 16
    START_POS = (1, 1)
    END_POS = (13, 13)
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(MAZE_SIZE)]
    result = 0
    visited = [[False] * MAZE_SIZE for _ in range(MAZE_SIZE)]
    queue = deque([START_POS])
    while queue:
        ci, cj = queue.popleft()
        FLAG = False
        for dx, dy in dxy:
            ni, nj = ci + dx, cj + dy
            if ni < 0 or ni >= MAZE_SIZE or nj < 0 or nj >= MAZE_SIZE: continue
            if visited[ni][nj]: continue
            if maze[ni][nj] == 1: continue
            queue.append((ni, nj))
            visited[ni][nj] = True
            # FLAG를 넣은 이유
            # 도착지에 도착한 다음에 break 하지만, 이 break는 for문밖에 나가지 못하기 때문에
            # 더 밖에 있는 while도 빠져나가기 위해서 FLAG를 설정하고
            # FLAG가 True라는 것은 도착지에 도착했다는 의미기 떄문에 큐에 들어있는 정점을 무시하고 break를 진행한다.
            if (ni, nj) == END_POS:
                result = 1
                FLAG = True
                break
        if FLAG:
            break
    print(f"#{tc} {result}")

# 빠른길찾기 BFS
from collections import deque
# 1. 전체 공간을 복사해서 각 공간의 좌표마다
# 시작지점에서 얼마나 이동했는 지를 저장하는 방식으로 구현
# 장점: 모든 목적지의 최단 거리를 알 수 있다. ( 조건, 시작지점 (0,0) 에서 시작한다는 조건)
# 단점: 메모리를 2배로 차지한다. ( 어차피 방문처리를 해야해서 어쩔 수없는 메모리입니다)
def get_road_move_time(road, n, m):
    # 4방향 탐색을 해야한다.
    # 하, 우, 상, 좌
    # dxy를 for loop로 돌면서 현재 좌표에 dx, dy를 더해주면, 상하좌우로 이동할 수 있다.
    dxy = [[1,0], [0,1], [-1,0], [0, -1]]
    # BFS는 큐로 구현 => deque
    # 문제에서는 [1,1] => [n,m]
    # 입력값을 [0,0] => [n-1, m-1]
    queue = deque([(0, 0)])
    # 복사하고, 각 좌표까지 걸리는 최단 이동거리를 저장해야된다.
    # m = 3 , [-1] * 3 => [-1, -1, -1]
    # 노드가 한 번 방문한 적이 있는 지 확인하는 용도로도 사용이 된다.
    # 해당 좌표까지의 이동 거리
    # -1로 꼭 초기화하지 않아도 된다. 자유롭게 초기화하자
    distance = [[-1] * m for _ in range(n)]
    distance[0][0] = 0  # 처음 시작 부분은 0 으로 하기로 문제가 정했다.
    while queue:  # 큐가 빌때까지 원소를 꺼내고 방문하는 행위를 반복한다.
        x, y = queue.popleft()
        for dx, dy in dxy:  # dxy = [[1,0], [0,1], [-1,0], [0, -1]]
            nx, ny = x + dx, y + dy  # 현재 위치에서 각 방향으로 이동
            # [nx, ny]가 갈 수 있는 곳인지를 체크해야한다.
            # 1. 도로 범위안에 포함될 것
            # 2. 방문한 적이 없을 것 (내가 갈 곳이 (-1) 이여야 한다)
            # 3. 갈 수 있는 곳일 것 (길이여야 한다. (1) 이여야 한다)
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and road[nx][ny] == 1:
                # 위 조건을 다 만족했으므로, 이동할 수 있는 좌표
                queue.append((nx, ny))
                # 현재 위치까지 오는데 걸린 이동 횟수 + 1 값을
                # 다음에 이동해야 할 좌표에 입력을 한다.
                distance[nx][ny] = distance[x][y] + 1
                if nx == n-1 and ny == m-1:
                    return distance[nx][ny]
    # while 문을 빠져 나왔다는 소리는, 결국 목적지에 도착하지 못했다!
    # 목적지를 찾지 못하면 "어떤 걸" 출력하세요 !! (문제에서 제시가 됨)
    # 제시된 걸 반환하면 된다.
    return -1  # -1도 제가 임의로 -1이라고 한거고요..
n, m = map(int, input().split())  # 도로의 크기 n * m 입력 받기
road = [list(map(int, input())) for _ in range(n)]  # 도로 정보 입력
# BFS를 이용해서 이동시간 구하기
result = get_road_move_time(road, n, m)
print(result)

# 섬 덩어리 찾기 BFS
from collections import deque
def find_island(island, x, y):
    # 상하좌우 + 대각선
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
    queue = deque([(x, y)])
    island[x][y] = 0  # 바다로 바꾸는 거에요 ( 방문 처리 하고, 겸사겸사 다음 BFS도 못들어오게 한다 )
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx +dx, cy + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if island[nx][ny] == 0:  # 바다인 경우
                continue
            queue.append((nx, ny))
            island[nx][ny] = 0
n, m = map(int, input().split())  # 섬의 크기 입력
arr = [list(map(int, input())) for _ in range(n)]  # 섬의 상태 입력 받기
island_cnt = 0  # 섬의 개수
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:  # 1이 땅이니까, 땅이면 BFS 실행
            find_island(arr, i, j)
            island_cnt += 1
print(island_cnt)  # 섬의 개수 출력

# 이진 탐색 트리
class Node:
    def __init__(self, key):
        self.key = key  # 노드의 값
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드
class BST:  # 2진탐색트리
    def __init__(self):
        self.root = None  # 루트 노드를 초기화
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)  # 트리가 비어 있으면 루트 노드로 설정
        else:
            self._insert(self.root, key)  # 재귀적으로 삽입
    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)  # 왼쪽 자식이 없으면 왼쪽에 삽입
            else:
                self._insert(node.left, key)  # 왼쪽 자식이 있으면 재귀적으로 삽입
        else:
            if node.right is None:
                node.right = Node(key)  # 오른쪽 자식이 없으면 오른쪽에 삽입
            else:
                self._insert(node.right, key)  # 오른쪽 자식이 있으면 재귀적으로 삽입
    def delete(self, key):
        self.root = self._delete(self.root, key)  # 루트 노드부터 재귀적으로 삭제
    def _delete(self, node, key):
        if node is None:
            return node  # 노드가 없으면 그대로 반환
        if key < node.key:
            node.left = self._delete(node.left, key)  # 왼쪽 서브트리에서 삭제
        elif key > node.key:
            node.right = self._delete(node.right, key)  # 오른쪽 서브트리에서 삭제
        else:
            if node.left is None:
                return node.right  # 왼쪽 자식이 없으면 오른쪽 자식을 반환
            elif node.right is None:
                return node.left  # 오른쪽 자식이 없으면 왼쪽 자식을 반환
            temp = self._minValueNode(node.right)  # 오른쪽 서브트리의 최소값 노드를 찾음
            node.key = temp.key  # 현재 노드의 키를 최소값 노드의 키로 대체
            node.right = self._delete(node.right, temp.key)  # 최소값 노드를 삭제
        return node
    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left  # 왼쪽 자식이 없을 때까지 이동하여 최소값 노드를 찾음
        return current
    def search(self, key):
        return self._search(self.root, key)  # 루트 노드부터 재귀적으로 검색
    def _search(self, node, key):
        if node is None or node.key == key:
            return node  # 노드가 없거나 값을 찾으면 해당 노드를 반환
        if key < node.key:
            return self._search(node.left, key)  # 왼쪽 서브트리에서 검색
        return self._search(node.right, key)  # 오른쪽 서브트리에서 검색
    def inorder(self):
        self._inorder(self.root)  # 중위 순회 시작
        print()
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)
# BST 생성
bst = BST()
bst.insert(10)  #처음이라 루트
bst.insert(5)  #두번째라 왼
bst.insert(15)  #오른
bst.inorder()
