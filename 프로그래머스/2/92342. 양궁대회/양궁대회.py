from collections import deque
def rec(n,idx,arr,info):
    global cache,trace
    if n<0:
        return -99999999999999999
    if idx==len(arr):
        return 0
    if cache[n][idx]!=-1:
        return cache[n][idx][0]
    a=rec(n,idx+1,arr,info)
    if info[idx]==0:
        b=rec(n-arr[idx][1],idx+1,arr,info)+arr[idx][0]
    else:
        b=rec(n-arr[idx][1],idx+1,arr,info)+arr[idx][0]*2
    if a>b:
        cache[n][idx]=[max(a,b),'a']
    elif a<b:
        cache[n][idx]=[max(a,b),'b']
    else:
        cache[n][idx]=[max(a,b),'ab']

    return max(a,b)
def solution(n, info):
    answer = []
    arr=[]
    for i in range(len(info)):
        arr.append([10-i,info[i]+1])
    global cache
    cache=[[-1] * len(info) for i in range(n+1)]
    rec(n,0,arr,info)
    origin_n=n
    q=deque([[n,0,[]]])
    while len(q):
        b=q.popleft()
        n,idx,tmp=b[0],b[1],b[2]

        while idx<len(arr):
            #print(n,idx)
            if cache[n][idx]==-1:
                print('error')
                break
            if idx==len(arr)-1:
                tmp.append(n)
                idx+=1
                break
            if cache[n][idx][1]=='a':
                idx+=1
                tmp.append(0)
            elif cache[n][idx][1]=='b':
                n-=arr[idx][1]
                tmp.append(arr[idx][1])
                idx+=1
            else:
                tmp.append(0)
                a1=tmp.copy()
                q.append([n,idx+1,a1])
                tmp.pop()
                tmp.append(arr[idx][1])
                a2=tmp.copy()
                q.append([n-arr[idx][1],idx+1,a2])
                break
        if idx==len(arr):
            answer.append(tmp)
    #print(answer)
    last=-1
    how_many=-1
    a=[]
    #print(answer)
    answer.sort(key=lambda x: tuple([-x[i] for i in range(10,-1,-1)]))
    if len(answer)>=1:
        answer=answer[0]

    lion=0
    apeach=0
    for i in range(len(answer)):
        if answer[i]==0 and info[i]==0:
            continue
        if answer[i]>info[i]:
            lion+=10-i
        elif answer[i]<=info[i]:
            apeach+=10-i
    print(lion,apeach)
    if lion<=apeach:
        return [-1]
    return answer