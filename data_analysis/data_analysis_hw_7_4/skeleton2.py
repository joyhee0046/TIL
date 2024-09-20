import pandas as pd

# 데이터 로드
file_path = _________
data = pd.read_csv(file_path, parse_dates=['Date'])

# 특정 기간(예: 2023년 상반기) 필터링
filtered_data = ________________

# 필터링된 데이터 확인
print(filtered_data.head())
