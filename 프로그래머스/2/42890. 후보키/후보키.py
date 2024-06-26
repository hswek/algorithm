from itertools import combinations
def is_unique(l,relation):
    d={}
    for tup in relation:
        tmp=''
        for a in l:
            tmp+=tup[a]
        if tmp in d:
            return False
        else:
            d[tmp]=True
    return True
def is_in_all(l1,l2):
    for i in l1:
        if i not in l2:
            return False
    return True
def is_mini(answer,l):
    for a in answer:
        if is_in_all(a,l):
            return False
    return True
def solution(relation):
    answer = []
    arr=range(0,len(relation[0]))
    for i in range(1,len(relation[0])+1):
        l=list(combinations(arr,i))
        for ll in l:
            if is_mini(answer,ll) and is_unique(ll,relation) :
                answer.append(ll)
            
                
        
    return len(answer)