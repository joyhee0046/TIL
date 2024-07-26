'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 아래에 코드를 작성하시오.
#ctrl + d, 포커싱으로 같은 단어 모두 수정(찾기)가능
score_dict = {"Alice" : 85, "Bob" : 78, "Charlie" : 92,  "David" : 88, "Eve" : 95}
print("1. 학생들의 이름과 점수를 딕셔너리에 저장")
print("students type:", type(score_dict))
print("학생들의 이름과 점수:", score_dict)

ave_score = sum(score_dict.values())/len(score_dict)
print("2. 모든 학생의 평균 점수:", f"{ave_score:.2f}")

# high=[]
# for k,v in score_dict.items():
#    if v >= 80 :
#       high.append(k)
# print(high)
high = [k for k,v in score_dict.items() if v >= 80 ]
print("3. 기준 점수(80점) 이상을 받은 학생 수:", high)

sor = dict(sorted(score_dict.items(), key=lambda x: x[1], reverse=True))  
#들어오는 값을 x라고 정의하고: x중에 1자리 값_인덱스1이라서 두번째값_을 이용할것.
i = 0
print("4. 점수순으로 정렬:")
print(*[f"{k}: {v}" for k,v in sor.items()],sep= "\n")

#ctrl + alt + 방향키, 포커싱 커서 증가
f2l = max(sor.values())-min(sor.values())
print("5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이:", f2l)

#ave_high = [True if i >= ave_score else False for i in score_dict.values()]
print("6. 각 학생의 점수가 평균보다 높은지 낮은지 판단:")

# for k in score_dict :
#     if score_dict[k] > ave_score :
#         status = "이상"
#     else :
#         status = "이하"
#     print(f'{key} 학생의 점수({score_dict[k]})는 평균 {status}입니다.')

print(
    *[f"{k} 학생의 점수({v})는 평균 이상입니다." 
      if v>= ave_score 
      else f"{k} 학생의 점수({v})는 평균 이하입니다." 
      for k,v in score_dict.items()],sep= "\n")