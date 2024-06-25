import sys
from collections import deque
import heapq
#sys.setrecursionlimit(10**4)
T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    reg,end=map(int,sys.stdin.readline().rstrip().split())
    
    q=deque()
    q.append([0,reg,-1])
    where=0
    parent_arr=[-1]
    visit=[-1]*11001
    while True:
        num,reg,parent=q.popleft()

        if reg==end:
            print_arr=[]
            while True:
                if parent==-1:
                    break
                print_arr.append(parent_arr[parent][0])
                parent=parent_arr[parent][1]
            for i in range(len(print_arr)-1,-1,-1):
                print(print_arr[i],end='')
            print()
            break        
        #D
        tmp_reg=reg*2%10000
        if visit[tmp_reg]!=0:
            visit[tmp_reg]=0
            where+=1
            parent_arr.append(['D',parent])
            q.append([num+1,tmp_reg,where])
        #S
        tmp_reg=(reg+9999)%10000
        if visit[tmp_reg]!=0:
            visit[tmp_reg]=0
            where+=1
            parent_arr.append(['S',parent])
            q.append([num+1,tmp_reg,where])
        #L
        tmp_reg=(reg*10+ reg//1000)%10000

        if visit[tmp_reg]!=0:
            visit[tmp_reg]=0
            where+=1
            parent_arr.append(['L',parent])
            q.append([num+1,tmp_reg,where])
        #R
        tmp_reg=((reg//10)+reg%10*1000)%10000
        if visit[tmp_reg]!=0:
            visit[tmp_reg]=0
            where+=1
            parent_arr.append(['R',parent])
            q.append([num+1,tmp_reg,where])