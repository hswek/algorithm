cache={}
def get(i,j,oper,arr):
    s=0
    cs=str(i)+"_"+str(j)+str(oper)
    if cs in cache:
        return cache[cs]
    if oper==max:
        tmp=-999999999999999999
        next_oper=min
    if oper==min:
        tmp=99999999999999999999
        next_oper=max
    for z in range(i,j):
        w=arr[z]
        if w.isdigit():
            s+=int(w)
        elif w=='-':
            for jj in range(z+1,j+1,2):
                tmp=oper(tmp,-get(z+1,jj+1,next_oper,arr)+get(jj+1,j,oper,arr))
            s+=tmp
            cache[cs]=s
            return s
    cache[cs]=s
    return s                         
def solution(arr):
    return get(0,len(arr),max,arr) 