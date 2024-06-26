def solution(cards):
    answer = 0
    d={}
    arr=[]
    for c in cards:
        if c in d:
            continue
        else:
            tmp=[]
            d[c]=True
            while True:
                tmp.append(c)
                c=cards[c-1]
                if c in d:
                    break
                d[c]=True
            arr.append(len(tmp))
    m=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            m=max(m,arr[i]*arr[j])     
    return m