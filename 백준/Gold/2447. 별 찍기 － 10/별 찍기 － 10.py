import sys
def fact(n,start):
    if n==3:
        arr[start].append('***')
        arr[start+1].append('* *')
        arr[start+2].append('***')
        return
    for i in range(3):
        fact(n//3,start)
    fact(n//3,start+n//3)
    for i in range(n//3):
        arr[start+n//3+i].append(' '*(n//3))
    fact(n//3,start+n//3)
    for i in range(3):
        fact(n//3,start+n//3*2)
    
n=int(input())
arr=[[] for i in range(n+1)]
fact(n,1)
for i in range(len(arr)):
    if i==0:
        continue
    for j in range(len(arr[i])):
        print(arr[i][j],end='')
    print()
