import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 평균이 0이고 표준편차가 1인 정규분포 데이터를 1000개 생성
data = ___________

# 히스토그램과 KDE 시각화
plt.figure(figsize=(10, 6))
sns.histplot(_______, bins=30, kde=____)
plt.title('Histogram with KDE of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
