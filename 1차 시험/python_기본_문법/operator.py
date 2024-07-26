'''
연산자
기본연산자와 복합연산자.
==는 동등성을 확인하는 연산자 is는 식별성(같은 객체를 참조하는 지)을 확인하는 연산자.
논리연산자.
맴버십 연산자. 다른 시퀀스나 컬렉션에 속하는지 여부 확인.
시퀀스 연산자. 시퀀스 간의 연산
'''

print(3 > 6)  # False
print(2.0 == 2)  # True
print(2 != 2)  # False
print('HI' == 'hi')  # False
print(1 == True)  # True

# SyntaxWarning: "is" with a literal. Did you mean "=="?
# ==은 값(데이터)을 비교하는 것이지만 is는 레퍼런스(주소)를 비교하기 때문. 데이터 흐름 확인.
# 아래 조건은 항상 False이기 때문에 is 대신 ==를 사용해야 한다는 것을 알림
print(1 is True)  # False
print(2 is 2.0)  # False


#단축평가의 경우, 결과로 앞뒤중 뭐가 나오는지 확인 필요.
vowels = 'aeiou'
print(('a' and 'b') in vowels)  # False
print(('b' and 'a') in vowels)  # True
print(('a' or 'b') in vowels)  # True
print(('b' or 'a') in vowels)  # False
print(3 and 5)  # 5
print(3 and 0)  # 0
print(0 and 3)  # 0
print(0 and 0)  # 0
print(5 or 3)  # 5
print(3 or 0)  # 3
print(0 or 3)  # 3
print(0 or 0)  # 0

word = 'hello'
numbers = [1, 2, 3, 4, 5]
print('h' in word)  # True
print('z' in word)  # False
print(4 not in numbers)  # False
print(6 not in numbers)  # True

# Gildong Hong
print('Gildong' + ' Hong')
# hihihihihi
print('hi' * 5)

# [1, 2, 'a', 'b']
print([1, 2] + ['a', 'b'])
# [1, 2, 1, 2]
print([1, 2] * 2)