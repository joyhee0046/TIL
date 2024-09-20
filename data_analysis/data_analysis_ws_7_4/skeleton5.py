import pandas as pd

# 데이터 로드
file_path = ______________
data = _____________

# 결측치 처리 전 데이터 저장
before_processing = data.copy()

# 결측치 처리 및 새로운 파생 변수 생성
data['column_with_missing'] = _________________
data['new_feature'] = data['column_1'].apply(___________)  # 'column_1'을 기준으로 새로운 파생 변수 생성

# 결측치 처리 후 데이터 비교
print("Before processing:")
print(before_processing.describe())
print("\nAfter processing:")
print(data.describe())
