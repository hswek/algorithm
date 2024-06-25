import sys
from collections import deque
              
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
s=sys.stdin.readline().rstrip()
arr2=0
for i in range(len(s)):
    #print(s[i])
    if s[i]=='Y':
        arr2+=2**i

m=int(sys.stdin.readline().rstrip())
def bit_count(a):
    if a==0:
        return 0
    return a%2+ bit_count(a//2)
rr=0
def recursive(arr2):
    global rr
    if cache[arr2]!=-1:
        return cache[arr2]
    #print(arr2)
    #print(bit_count(arr2))
    if bit_count(arr2)>=m:
        #print(bin(arr2))
        rr=1
        return 0
    result=987654321
    for i in range(n):
        if (arr2 & (1<<i)) == 0:
            min_num=987654321
            go=-1
            for j in range(n):
                if i==j or (arr2 & (1<<j)) == 0 :
                    continue
                if min_num>arr[j][i]:
                    min_num=arr[j][i]
                    go=j
            if go==-1:
                continue
            #print(go)
            result=min(result, recursive(arr2 | 1<<i  )+min_num)
    cache[arr2]=result
    return result
cache=[-1]*(2**n+1)
r=recursive(arr2)
if r>=98765432 and rr==1:
    print(0)
elif rr==0:
    print(-1)
else:
    print(r)