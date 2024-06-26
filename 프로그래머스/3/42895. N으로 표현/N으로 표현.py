def solution(N, number):
    answer = 0
    d={0:{}}
    for i in range(1,10):
        d[i]={}
        r=[]
        for j in range(1,i):
            for key in d[j].keys():
                for key2 in d[i-j].keys():
                    r.append(key+key2)
                    r.append(key-key2)
                    r.append(key*key2)
                    if key2!=0:
                        r.append(key/key2)
        for rr in r:
            d[i][rr]=1
        d[i][int(str(N)*i)]=1
        #print(i,d)
        if number in d[i]:
            return i
    return -1