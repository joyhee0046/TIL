def age18(dict) :
    ag = []
    for i in dict : 
        if i['age'] >=18 :
            ag.append(i)
    return ag

def actT(dict) :
    ac = []
    for i in dict : 
        if i['is_active'] == True :
            ac.append(i)
    return ac
    
def age_act(dict) :
    agac=[]
    for i in dict : 
        if i['age'] >=18 and i['is_active'] == True:
            agac.append(i)
    return agac




# def is_adult(user):
#     if user["age"] >= 18:
#         return True


# def is_active_user(user):
#     return user["is_active"]


# def is_adult_active_user(user):
#     if is_adult(user) and is_active_user(user):
#         return True
#     else:
#         return False