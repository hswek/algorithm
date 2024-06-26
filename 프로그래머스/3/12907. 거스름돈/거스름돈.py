def solution(n, money):
    answer = 0
    cache=[0]*(n+1)
    cache[0]=1
    for m in money:
        for i in range(1,n+1):
            #print(i,m)
            if i-m>=0:
                
                cache[i]=cache[i]+cache[i-m]%1000000007
    #print(cache)
    return cache[n] %1000000007