def solution(a, b, g, s, w, t):
    answer = 0
    n=len(g)
    start=0
    end=9999999999999999999
    while start+1<end:
        gc=0
        sc=0
        tc=0
        mid=(start+end)//2
        for i in range(len(g)):
            num=(mid)//(t[i]*2)
            if mid%(t[i]*2)>=t[i]:
                num+=1
            gc+=min(g[i],w[i]*num)
            sc+=min(s[i],w[i]*num)
            tc+=min(g[i]+s[i],w[i]*num)
        if gc>=a and sc>=b and tc>=a+b:
            end=mid
        else:
            start=mid
    return start+1