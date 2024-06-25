import sys
n,k=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
dp=[0]*(k+1)
dp[0]=1
for i in arr:
    for j in range(k+1):
        if j>=i:
            dp[j]=dp[j]+dp[j-i]
#print(dp)
print(dp[k])