import sys
def bit_len(tmp):
    #print(tmp)
    if tmp==0:
        return 0
    return tmp%2+bit_len(tmp//2)

def recursive(n,m,pos,last):
    global cache,arr
    if pos==n:
        return 0
    #print(pos,last)
    if cache[last][pos]!=-1:
        return cache[last][pos]
    tmp=arr[pos]
    #print(pos,tmp)
    for i in range(1,m-1):
        if last & (1<<i):
            tmp=tmp & ~( 1<<(i+1))
            tmp=tmp & ~( 1<<(i-1))
    if last & (1<<0):
        tmp=tmp & ~(2)
    if last & (1<<(m-1)):

        tmp=tmp & ~( 1<<(m-2))
    tmp2=tmp
    result=0
    a=1
    #print(pos,last,bin(tmp2))
    while True:

        a=0
        for i in range(m):
            if (tmp & (1<<i)) and (tmp & (1<<(i+1))):
                #print('aaa',bin(tmp))  
                a=1
                break
        if a==1:
            tmp=(tmp-1) & tmp2
            continue
        #print(bin(tmp))     
        result=max(result,recursive(n,m,pos+1,tmp) + bit_len(tmp))
        if tmp==0:
            break
        tmp=(tmp-1) & tmp2
    #print(last,pos)
    cache[last][pos]=result
    #print(pos,last,result)
    return result
    
def solve():
    global cache,arr
    n,m=map(int,sys.stdin.readline().rstrip().split())
    arr=[]
    for i in range(n):
        arr.append(list(sys.stdin.readline().rstrip()))
    #print(arr)
    for i in range(n):
        tmp=0
        for j in range(m):
            if arr[i][j]!='x':
                #print(arr[i][j])
                #print(j)
                tmp=tmp|2**(m-j-1)
        arr[i]=tmp
    #print(arr)
    cache=[[-1]*11 for i in range(2**(m+1))]
    print(recursive(n,m,0,0))
        


t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    solve()