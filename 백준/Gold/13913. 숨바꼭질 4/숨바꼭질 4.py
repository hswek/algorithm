import sys
from collections import deque
sys.setrecursionlimit(10**5)
subin,sister=map(int,sys.stdin.readline().rstrip().split())
visit=[0]*100010

d=deque()
d.append([subin,0,-1])
memorize=[-1]*(100010)
where=0
print_arr=[]
while(len(d)!=0):
    now,a,tmp=d.popleft()
    if now== sister:
        print(a)
        
        while (True):
            if tmp==-1:
                break
            print_arr.append(memorize[tmp][1])
            tmp=memorize[tmp][0]

        #print(print_arr)
        print(subin,end=' ')
            
        for i in range(len(print_arr)-1,-1,-1):
            subin+=print_arr[i]
            print(subin,end=' ')


        break
    pos=[1,-1,now]
    for i in pos:
        nx=now+i
        if nx>=100001 or nx<0 or visit[nx]==1:
            continue
        visit[nx]=1
        where+=1
        memorize[where]=[tmp,i]
        d.append([nx,a+1,where])
    