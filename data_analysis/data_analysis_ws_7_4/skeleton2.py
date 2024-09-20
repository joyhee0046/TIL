import pandas as pd

# 데이터 로드
file_path = ______________
data = ______________

# 결측치가 있는 열 확인
missing_data = ____________

# 결측치가 있는 열 및 결측치 개수 출력
print("Missing values in each column:")
print(________________)

# 결측치 제거 또는 대체 (여기서는 평균값으로 대체 예시)
data['column_with_missing'] = ________________

# 결측치 처리 후 데이터 확인
print(data.info())
