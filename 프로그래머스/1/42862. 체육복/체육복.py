
        
def solution(n, lost, reserve):
    answer = 0
    l={}
    r={}
    for i in lost:
        l[i]=1
    for i in reserve:
        if i not in l:
            r[i]=1
        else:
            del l[i]
    new_lost=list(l.keys())
    new_lost.sort()
    new_lost_copy=new_lost.copy()
    #print(new_lost)
    new_reserve=list(r.keys())
    new_reserve.sort()
    for i in new_lost_copy:
        #print(i)
        if i-1 in new_reserve:
            #print(i,1)
            new_lost.remove(i)
            new_reserve.remove(i-1)
        elif i+1 in new_reserve:
            #print(i,2)
            new_lost.remove(i)
            new_reserve.remove(i+1)
        
            #print(i,'가 못빌림')
    #print(new_lost)
    return n-len(new_lost)