def dfs(now,n,n2):
    if now>n2:
        return 998765311235
    if cache[now]<=n:
        return
    a=dfs(now,n+i,n2)+i
    b=dfs(now,n*2,n2)
    
def solution(n):
    ans = 0
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    while n!=0:
        if n%2==1:
            n-=1
            ans+=1
        else:
            n=n//2
    
    return ans