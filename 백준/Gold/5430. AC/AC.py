import sys
from collections import deque
re=int(input())
for i in range(re):
    order=input()
    n=int(input())
    l=input()
    
    if(n!=0):
        l=list(map(int,l[1:len(l)-1].split(",")))
    else:
        l=[]

    #print(l)
    l=deque(l)
    what=0
    reverse=False
    error=False
    for j in range(len(order)):
        if order[j]=="R":
            if reverse==True:
                reverse=False
            else:
                reverse=True
        if order[j]=="D":
            if len(l)==0:
                print("error")
                error=True
                break   
            if reverse==True:
                l.pop()
            else:
                l.popleft()
    if error==True:
        continue
    if reverse==True:
        l.reverse()

    s="["
    for i in range(len(l)):
        s=s+str(l[i])+","
    if(len(s)!=1):
        s=s[:len(s)-1]
    s=s+"]"
    
    print(s)
