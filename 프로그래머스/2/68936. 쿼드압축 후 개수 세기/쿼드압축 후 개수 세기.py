def is_all_same(arr,x,y,x2,y2):
    a=arr[x][y]
    for i in range(x,x2):
        for j in range(y,y2):
            if arr[i][j]!=a:
                return -1
    return a
def rec(arr,x,y,x2,y2):
    if x2-x==1:
        #print(x,y,x2,y2)
        if arr[x][y]==0:
            return [1,0]
        else:
            return [0,1]
    tmp=is_all_same(arr,x,y,x2,y2)
    if tmp!= -1:
        #p#rint(x,y,x2,y2)
        if tmp==0:
            return [1,0]
        else:
            return [0,1]
    midx=(x2-x)//2+x
    midy=(y2-y)//2+y
    a=rec(arr,x,y,midx,midy)
    b=rec(arr,midx,y,x2,midy)
    c=rec(arr,x,midy,midx,y2)
    d=rec(arr,midx,midy,x2,y2)
    return [a[0]+b[0]+c[0]+d[0],a[1]+b[1]+c[1]+d[1]]
def solution(arr):
    answer = rec(arr,0,0,len(arr),len(arr))
    
    return answer