
def recursive(number, _count):

    if _count == 0: return 1
    return number * recursive(number,_count - 1)

for _ in range(10):
    test_case = int(input())
    a, b = map(int, input().split())
    print(f"#{test_case} {recursive(a,b)}")

