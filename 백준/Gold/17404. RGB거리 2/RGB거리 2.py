import sys
#a,b=sys.stdin.readline().rstrip().split()
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
cache=[[[-1]* (3) for i in range(3)] for i in range(n)]
def recursvie(start,start_color,prev_color):
    m=9876543210
    if start==n:
        return 0
    if cache[start][start_color][prev_color]!=-1:
        return cache[start][start_color][prev_color]
    for i in range(3):
        if prev_color==i:
            continue
        if start==n-1:
            if i==start_color:
                continue
        m=min(m,recursvie(start+1,start_color,i)+arr[start][i])
    cache[start][start_color][prev_color]=m
    return m
    
    
m=9876543210
for i in range(3):
    m=min(m,recursvie(1,i,i)+arr[0][i])
print(m)