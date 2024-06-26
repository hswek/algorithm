def rec(n,l,r,now):
    result=''
    if n==0:
        return now[l:r+1]
    for i in range(len(now)):
        if r<0:
            break
        if 5**n<l:
            l-=5**n
            r-=5**n
            continue
        else:
            if now[i]=='0':
                nex='00000'
            else:
                nex='11011'
            result+=rec(n-1,l,r,nex)
            l-=5**n
            r-=5**n
            l=max(l,0)
    return result
def solution(n, l, r):
    now=rec(n,l-1,r-1,'1')
    #print(now)
    answer=0
    for i in now:
        if i=='1':
            answer+=1
    return answer