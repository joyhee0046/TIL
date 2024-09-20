import pandas as pd

# 데이터 로드
file_path = ______________
data = _____________

# 결측치 처리 및 새로운 파생 변수 생성
data['column_with_missing'] = ________________________
data['new_feature'] = data['column_1'].apply(___________)  # 'column_1'을 기준으로 새로운 파생 변수 생성

# 데이터 변환 후 요약
summary = data.describe()

# 요약 통계 출력
print(summary)
