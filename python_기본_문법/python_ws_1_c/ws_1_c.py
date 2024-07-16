# 아래에 코드를 작성하시오.
sys = [['O' for i in range(3)]for i in range(3)]
sys[0][2] = "X"
sys[1][0] = "X"
sys[1][2] = "X"
sys[2][0] = "X"
sys[2][2] = "X"

print("현재 좌석 배치: ")
for i in range(3) :
    print(*sys[i][:])