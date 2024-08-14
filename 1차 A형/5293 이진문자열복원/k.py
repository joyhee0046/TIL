# test_case = int(input())
# for t in range(test_case):
#     bi_dict = {
#         "00": 0,
#         "01": 0,
#         "10": 0,
#         "11": 0,
#     }
#
#     bi_cnt = list(map(int, input().split()))
#
#     bi_dict["00"] = bi_cnt[0]
#     bi_dict["01"] = bi_cnt[1]
#     bi_dict["10"] = bi_cnt[2]
#     bi_dict["11"] = bi_cnt[3]
#
#     result = 'impossible'
#     if bi_dict["01"] == 0 and bi_dict["10"] == 0:
#         if bi_dict["00"] == 0:
#             result = "1" * bi_dict["01"] + "1"
#         elif bi_dict["11"] == 0:
#             result = "0" * bi_dict["01"] + "0"
#
#     else:
#         if bi_dict["01"] == bi_dict["10"]:
#             result = "0"*bi_dict["00"] + "01"*(bi_dict["01"]) + "1"*bi_dict["11"] + "0"
#         elif bi_dict["01"] == bi_dict["10"] + 1:
#             result = "0"*bi_dict["00"] + "01"*(bi_dict["01"]) + "1"*bi_dict["11"]
#         elif bi_dict["01"] + 1 == bi_dict["10"]:
#             result = "1"*bi_dict["11"] + "10"*(bi_dict["10"]) + "0"*bi_dict["00"]
#         elif bi_dict["01"] == 0 and bi_dict["10"] == 1:
#             result = "1"*bi_dict["11"] + "10" + "0"*bi_dict["00"]
#         elif bi_dict["01"] == 1 and bi_dict["10"] == 0:
#             result = "0"*bi_dict["00"] + "01" +"1"*bi_dict["11"]
#
#     print(f"#{t+1} {result}")

test_case = int(input())
for t in range(test_case):

    cnt_00, cnt_01, cnt_10, cnt_11 = list(map(int, input().split()))

    result = 'impossible'
    if cnt_01 == 0 and cnt_10 == 0:
        if cnt_00 == 0:
            result = "1" * cnt_11 + "1"
        elif cnt_11 == 0:
            result = "0" * cnt_00 + "0"

    else:
        if cnt_01 == cnt_10:
            result = "0" * cnt_00 + "01" * (cnt_01) + "1" * cnt_11 + "0"
        elif cnt_01 == cnt_10 + 1:
            result = "0" * cnt_00 + "01" * (cnt_01) + "1" * cnt_11
        elif cnt_01 + 1 == cnt_10:
            result = "1" * cnt_11 + "10" * (cnt_10) + "0" * cnt_00
        elif cnt_01 == 0 and cnt_10 == 1:
            result = "1" * cnt_11 + "10" + "0" * cnt_00
        elif cnt_01 == 1 and cnt_10 == 0:
            result = "0" * cnt_00 + "01" + "1" * cnt_11

    print(f"#{t + 1} {result}")