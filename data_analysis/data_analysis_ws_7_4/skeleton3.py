import pandas as pd

# 데이터 로드
file_path = _____________
data = ______________

# 결측치 처리 (이전 코드에서 이미 처리함)
data['column_with_missing'] = _____________________

# 새로운 파생 변수 생성 (예: 'column_1'의 제곱 값을 새로운 파생 변수로 추가)
data['new_feature'] = data['column_1'].apply(__________)

# 생성된 파생 변수 확인
print(data[['column_1', 'new_feature']].head())
