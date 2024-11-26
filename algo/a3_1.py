## 두 배
'''
두 배
양수와 음수로 이루어진 길이 N의 배열이 있다.
배열의 합이 2*N(N 곱하기 2) 이상이 될 수 있도록 해야한다.
임의의 i (0 <= i <= N-1)을 지정하여 A[i] = max(A[i]+i, i)로 바꿀 수 있다.
max(A[i] + i, i)는 A[i] + i 와 i 중 큰 값을 의미한다.
바꾸는 횟수를 최소로 해서 배열의 합이 2N 이상이 되는 횟수를 출력해라.
단 한번 변경한 값은 다시 바꿀 수 없다

예를들어, 1, -2, 2, 3으로 받게 될 때, 2번째인 -2를 max(A[1] + 2, 2)로 하여 2로 변환 할 수 있다. 그렇게 되면 1 + 2(변환된 수) + 2 + 3 = 8 ( >= 2 * 4) 이므로 최소 변환 횟수는 1이 된다.

각 테스트케이스에 첫번째 줄은 N, 두번째 줄은 배열을 의미한다
4 <= N <= 1000
'''
def universe():
    univ = [0]*n
    for i in range(n):
        univ[i] = max(arr[i]+i+1, i+1)
        univ[i] -= arr[i]
    return univ


def cal(num):
    global ans
    for i in range(n):
        num -= double[i]
        ans +=1
        if num <= 0:
            return


T = int(input())

for tc in range(T):
    ans = 0
    n = int(input())
    arr = list(map(int, input().split()))
    hap = 0
    for k in range(n):
        hap += arr[k]

    if hap < 2*n:
        double = universe()
        double.sort(reverse=True)
        need_num = 2*n - hap
        cal(need_num)

    print(f'#{tc+1}', ans)







'''
입력 예제
4
1 -2 2 3
출력 예제
1

입력 예제2
4
8 1 1 2
출력 예제2
0
'''