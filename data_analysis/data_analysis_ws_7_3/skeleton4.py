import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
file_path = ______________
data = _____________

# 열 이름 확인
print(data.columns)  # DataFrame의 열 이름을 출력하여 확인

# 히스토그램과 KDE 플롯 시각화
if 'column_name' in data.columns:  # 'column_name' 열이 있는지 확인
    plt.figure(figsize=(12, 6))
    sns.histplot(__________, kde=________)
    plt.title('Histogram and KDE of column_name')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("Column 'column_name' does not exist in DataFrame. Please check the column names above.")
