# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(10):
    # ///////////////////////////////////////////////////////////////////////////////////
    test_case = int(input())
    base, exp = map(int, input().split())
    
    def exponentiation(base, exp):
        if exp == 1:
            return base
        else:
            return base * exponentiation(base, exp - 1)
        
    print(f'#{test_case} {exponentiation(base, exp)}')
    # ///////////////////////////////////////////////////////////////////////////////////