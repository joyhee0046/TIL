import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
file_path = ___________
data = ____________

# 시간에 따른 특정 변수(column_1)의 변화 시각화
plt.figure(figsize=(12, 6))
plt.plot(________, __________, marker='o')
plt.title('Time Series of column_1')
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.show()
