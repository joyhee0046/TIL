# 아래에 코드를 작성하시오.
numbers = [i for i in range(1,11)]

for i in numbers :
    if i == 5 :
        break
    if i%2 ==0 : 
        print(i)
    else :
        print(f"{i}(은)는 홀수")