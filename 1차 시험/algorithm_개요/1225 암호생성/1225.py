import sys
sys.stdin = open("input.txt", 'r')


# for _ in range(0,10):
#     tc = int(input())
#     li = list(map(int,input().split()))
#     wh = True
#     while wh == True:
#         for i in range(1,6):
#                 if (li[0]-i) > 0:
#                     li.append(li[0]-i)
#                     li.pop(0)
#                     i+=1
#                 else:
#                     li.append(0)
#                     li.pop(0)
#                     wh = False
#                     break
#     print("#{}".format(tc), end=' ', sep='')
#     print(*li)


for _ in range(0, 10):
    tc = int(input())
    li = list(map(int, input().split()))
    while True:
        for i in range(1, 6):
                if (li[0]-i) > 0:
                    li.append(li[0]-i)
                    li.pop(0)
                    i+=1
                else:
                    li.append(0)
                    li.pop(0)
                    False
                    break
    print("#{}".format(tc), *li)