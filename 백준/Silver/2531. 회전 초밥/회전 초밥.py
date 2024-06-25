import sys
n,d,k,c=map(int,sys.stdin.readline().split())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
result=0
max_set={}
for start_idx in range(n):
    s={}
    is_c_contain=False
    for i in range(k):
        next_idx=(start_idx+i)%n
        next_dish=arr[next_idx]
        if next_dish not in s:
            s[next_dish]=1
        if next_dish==c:
            is_c_contain=True
    if is_c_contain==False:
        s[c]=1
    result=max(result,len(s))

print(result)
        
            