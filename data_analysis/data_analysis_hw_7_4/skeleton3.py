import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
file_path = ____________
data = pd.read_csv(file_path, parse_dates=['Date'])

# 특정 기간 필터링
filtered_data = ________________

# 시간에 따른 변화 시각화
plt.figure(figsize=(12, 6))
plt.plot(__________, _________, marker='o')
plt.title('Time Series Data (2023 H1)')
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.show()

# 특정 기간 동안의 평균값과 최대값 계산
mean_value = filtered_data['value'].mean()
max_value = filtered_data['value'].max()

print(f"2023년 상반기 평균값: {mean_value:.2f}")
print(f"2023년 상반기 최대값: {max_value:.2f}")
