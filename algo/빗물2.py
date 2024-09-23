import sys
sys.stdin = open('14719.txt', 'r')
T = int(input())
H, W = map(int, input().split())
li = list(map(int, input().split()))

leastdeep = 0
deep = 0
ans = 0
# max(li)
for i in range(W):
    if li[i] > leastdeep:
        leastdeep = li[i]
    ans += (leastdeep - li[i])
if ans == 0:
    print(ans)
    flag = False
else:
    flag = True
while flag:
    if li[i] != leastdeep:
        for i in range(W - 1, 0, -1):
            if li[i] == leastdeep:
                check = li[i + 1:]
                deep = max(check)
                if max(check) == li[-1]:
                    ans -= ((W - i - 1) * (leastdeep - deep))
                    flag = False
                    break
                leastdeep = max(check)
                ans -= ((W - i - 1) * (check[1] - check[i - 1]))
                flag = False
                break
    flag = False
    break

print(ans)