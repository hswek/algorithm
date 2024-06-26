def is_same(id1,id2):
    if len(id1)!=len(id2):
        return False
    for i in range(len(id1)):
        if id2[i]!=id1[i] and id2[i]!='*':
            #print(id1,id2,id1[i],id2[i])
            return False
    return True
def rec(arr,idx,dd,bit):
    global d,id_to_int
    if idx==len(arr):
        
        if bit in dd:
            return 0
        dd[bit]=True
        #print(bin(bit))
        return 1
    result=0
    for i in arr[idx]:
        if bit & 1<<id_to_int[i]:
            continue
        bit+=2**id_to_int[i]
        result+=rec(arr,idx+1,dd,bit)
        bit-=2**id_to_int[i]
    return result
def solution(user_id, banned_id):
    answer = 1
    arr=[]
    global id_to_int
    id_to_int={}
    for i in range(len(user_id)):
        id_to_int[user_id[i]]=i
    for ban in banned_id:
        tmp=[]
        for user in user_id:
            if is_same(str(user),str(ban))==True:
                #print(user,ban,is_same(user,ban))
                tmp.append(str(user))
        arr.append(tmp)
    global d
    d=[]
    answer=rec(arr,0,{},0)
    return answer