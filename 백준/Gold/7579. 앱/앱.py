import sys
n,m=map(int,sys.stdin.readline().rstrip().split())

memory_arr=list(map(int,sys.stdin.readline().rstrip().split()))
repair_arr=list(map(int,sys.stdin.readline().rstrip().split()))

cache=[[-1]*10001 for i in range(101)]

def recursive(pos,can_use_c):
    if pos!=-1 and cache[pos][can_use_c]!=-1:
        return cache[pos][can_use_c]
    if can_use_c<0:
        print('oops'*1000)
        return

    tmp=0
    for i in range(pos+1,n):
        if can_use_c-repair_arr[i]>=0:
            tmp=max(tmp,memory_arr[i]+recursive(i,can_use_c-repair_arr[i]))
    
    cache[pos][can_use_c]=tmp
    return tmp
for i in range(10001):
    if recursive(-1,i)>=m:
        print(i)
        break