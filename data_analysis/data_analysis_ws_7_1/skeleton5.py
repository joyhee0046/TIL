import numpy as np

# 평균이 0이고 표준편차가 1인 정규분포 데이터를 1000개 생성
data = ___________

# 평균과 표준편차 계산
mean = ___________
std_dev = __________

# 결과 출력 및 확인
print(f"Calculated Mean: {mean:.2f}")
print(f"Calculated Standard Deviation: {std_dev:.2f}")

# 생성된 데이터의 특성과 일치하는지 확인
if np._________(mean, 0, atol=0.1) and np.________(std_dev, 1, atol=0.1):
    print("The calculated mean and standard deviation are consistent with the generated data's characteristics.")
else:
    print("The calculated mean and standard deviation are not consistent with the generated data's characteristics.")
