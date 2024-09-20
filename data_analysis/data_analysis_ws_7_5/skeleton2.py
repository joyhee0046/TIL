import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
file_path = ___________
data = ___________

# 'Date' 열을 제외하고 상관관계 계산
correlation_matrix = data.drop(columns=______).______()

# 상관관계 히트맵 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(_____________, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
