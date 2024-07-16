#파이썬으로 깃 명령어 사용.
#모듈 2가지 os, subprocess
#os로 현재 작업 위치 확인
#현재 폴더 및 하위 폴더 반복할건데, subprocess로 반복실행의 역할
'''
subprocess.run(['문자열로','실행 명령어', 변수])
https://lab.ssafy.com/youghee0406/{과목}_{구분}_{세트번호}_{단계}.git
실습실에 생성되는 레포지토리 마다 URL이 다른데, string intertpolation을 하면 가능.
과목 : python, web, js, django, db, vue : 입력받기
구분 : hw, ws : 반복문으로 입력
세트번호 : 확인 필요 : 입력받기
단계 : 1, 2, 3, 4, 5 : range(1,6) _총 5단계
결과주소 : f"https://lab.ssafy.com/youghee0406/{과목}_{구분}_{세트번호}_{단계}.git")
'''

subject = input("과목명 : ")
sep = ['hw','ws']
set_num = input("세트번호 : ")
for i in 
if sep == "hw" :
    for j in range(1,6) :
else : 
    for j in range([2,4]) :

import os, subprocess
current_folcer = os.getcwd()


subprocess.run(['git','clone',])