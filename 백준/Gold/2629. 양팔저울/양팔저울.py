import sys
n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))

k=int(input())
k_arr=list(map(int,sys.stdin.readline().rstrip().split()))

dp=[0]*41000
dp[0]=1
for num in arr:
    dp_copy=dp.copy()
    for i in range(41000):
        if dp[i]!=0:
            dp_copy[i+num]=dp[i]+1
            if i-num>0:
                dp_copy[i-num]=dp[i]+1
            else:
                dp_copy[num-i]=dp[i]+1
    dp=dp_copy
#print(dp[:400])
for i in k_arr:
    if dp[i]!=0:
        print('Y')
    else:
        print('N')
