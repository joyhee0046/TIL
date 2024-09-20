import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
file_path = ______________
data = _____________

# 데이터의 열 이름 출력하여 확인
print(data.columns)

# 열 이름을 확인한 후, 존재하는 열 이름으로 수정
# 여기서 'column_name'을 실제 존재하는 열 이름으로 바꿔야 함
column_name_to_plot = 'column_name'  # 'column_name'을 데이터셋에 맞는 실제 열 이름으로 변경하세요.

if column_name_to_plot in data.columns:
    plt.figure(figsize=(8, 6))
    sns.boxplot(______________)
    plt.title(f'Boxplot of {column_name_to_plot}')
    plt.ylabel('Value')
    plt.show()
else:
    print(f"Column '{column_name_to_plot}' does not exist in DataFrame. Please check the column names above.")
