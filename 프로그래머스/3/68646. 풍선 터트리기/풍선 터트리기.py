def solution(a):
    answer = 0
    answer=min(len(a),2)
    prev=[-1]*len(a)
    prev[0]=a[0]
    for i in range(1,len(a)):
        prev[i]=min(prev[i-1],a[i])
    later=[-1]*len(a)
    later[-1]=a[-1]
    for i in range(len(a)-2,-1,-1):
        
        later[i]=min(later[i+1],a[i])
    #print(prev)
    #print(later)
    for i in range(1,len(a)-1):
        #print(i,prev[i-1],later[i+1])
        if not(prev[i-1]<a[i] and a[i]>later[i+1]):
            answer+=1
            
    return answer