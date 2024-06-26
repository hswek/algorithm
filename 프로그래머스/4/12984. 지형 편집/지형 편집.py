from itertools import chain
def solution(land, p, q):
    l=[]
    for ll in land:
        l+=ll
    l.append(0)
    l.sort()
    n=len(land)**2
    cost=sum(l)*q
    ans=cost
    for i in range(len(l)):
        if i==0:
            continue
        else:
            if l[i]!=l[i-1]:
                cost=cost+(l[i]-l[i-1])*(i-1)*p - (l[i]-l[i-1])*(n-i+1)*q
                if cost>ans:
                    return ans
                ans=cost
    return ans
    
   