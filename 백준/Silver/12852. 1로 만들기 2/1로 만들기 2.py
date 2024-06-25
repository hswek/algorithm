import sys
from collections import deque
import heapq
import bisect
n=int(input())
q=deque()
q.append([n,0,0])
where=0
arr=[0]*(10*n)
while True:
    top,num,start=q.popleft()
    if top==1:
        print(num)
        print_arr=[]
        while True:
            if start==0:
                break
            #print('start',start)
            print_arr.append(arr[start][1])
            start=arr[start][0]
        print(n,end=' ')
        for i in range(len(print_arr)-1,-1,-1):
            if print_arr[i]==1:
                n=n//3
                print(n,end=' ')
            if print_arr[i]==2:
                n=n//2
                print(n,end=' ')
            if print_arr[i]==3:
                n=n-1
                print(n,end=' ')
        break
    if top%3==0:
        where+=1
        arr[where]=[start,1]
        q.append([top//3,num+1,where])
    if top%2==0:
        where+=1
        arr[where]=[start,2]
        q.append([top//2,num+1,where])
    where+=1
    arr[where]=[start,3]
    q.append([top-1,num+1,where])