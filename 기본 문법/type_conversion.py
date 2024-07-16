# 암시적 형변환. 파이썬의 내부동작으로 자동으로 형변환이 이뤄지는 것.
#Boolean과 Numeric에서만 가능.
print(3 + 5.0)  # 8.0
print(True + 3)  # 4
print(True + False)  # 1


# 명시적 형변환. 개발자가 직접 형변환을 하는 것.
print(int('1'))  # 1


# ValueError: invalid literal for int() with base 10: '3.5'
print(int('3.5'))

print(int(3.5))  # 3
print(float('3.5'))  # 3.5

print(str(1) + '등')  # 1등