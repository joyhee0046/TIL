import pandas as pd
# import matplotlib.pyplot as plt
import datetime

# 데이터 로드
file_path = pd.read_csv('stock_data.csv')
stock_data = file_path
print(stock_data)

# 날짜 데이터에서 월 정보 추출
stock_data = stock_data.to_datetime()
print(stock_data)
stock_data['Month'] = stock_data['Date'].dt.month
print(stock_data)

# # 월별 종가 평균 계산
# monthly_avg = ___________
#
# # 월별 종가 평균 시각화
# plt.figure(figsize=(10, 6))
# ________________
# plt.title('Monthly Average Closing Price')
# plt.xlabel('Month')
# plt.ylabel('Average Close Price (KRW)')
# plt.xticks(rotation=45)
# plt.show()
