def bino(n, k):
	# 배열 초기화
	B = [[0 for _ in range(k+1)] for _ in range(n+1)]
	# dp테이블 채우기
	for i in range(n+1):
		for j in range(min(i,k)+1):
			# 기본 케이스
			if j==0 or j==i:
				B[i][j] = 1
			else:
				# 이항계수 계산
				B[i][j] = B[i-1][j-1] + B[i-1][j]
	# nCk값 반환
	return B[n][k]
print(bino(5,2))