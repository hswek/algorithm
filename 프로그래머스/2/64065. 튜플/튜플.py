def solution(s):
    answer = []

    s=s[1:-1]
    s=s.split('}')
    tmp=[]
    for i in s:
        i=i.replace('{','')
        i=i.split(',')
        tmp.append(i)
    s=tmp
    tmp=[]
    for i in s:
        a=[]
        for j in i:
            if j=='':
                continue
            else:
                #print(j)
                a.append(int(j))
        tmp.append(a)
    s=tmp
        
    s.sort(key= lambda a:len(a))
    d={}

    for set1 in s:
        for j in set1:
            if j in d:
                continue
            else:
                d[j]=True
                answer.append(int(j))
        
    
    
    return answer