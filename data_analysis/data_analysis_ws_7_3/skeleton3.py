import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
file_path = ____________
data = _____________

# 기본적인 기술 통계 계산
statistics = ____________

# 기술 통계량 바 차트로 시각화
plt.figure(figsize=(12, 6))
statistics.loc[['mean', '50%', 'min', 'max', 'std']].______(kind=______)
plt.title('Basic Statistics of the Dataset')
plt.xlabel('Statistics')
plt.ylabel('Value')
plt.xticks(rotation=0)
plt.show()
