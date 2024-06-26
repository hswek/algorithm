def solution(words, queries):
    answer = []
    d={}
    check_d=[]
    for word in words:
        if len(word)<5000:
            now_string=""
            for i in range(len(word)):
                if now_string+ word[i:] not in d:
                    d[now_string+ word[i:]]=0
                d[now_string+ word[i:]]+=1
                now_string+="?"
            now_string=""
            for i in range(len(word)):
                if  now_string+"?"*(len(word)-i) not in d:
                    d[ now_string+"?"*(len(word)-i)]=0
                d[ now_string+"?"*(len(word)-i)]+=1
                now_string+=word[i]
        else:
            check_d.append(word)    
    for query in queries:
        if query in d:
            result=d[query]
        else:
            result=0
        for word in check_d:
            if len(word)!=len(query):
                continue
            is_same=True
            for i in range(len(word)):
                if query[i]!="?" and query[i]!=word[i]:
                    is_same=False
                    break
            if is_same==True:
                result+=1
        answer.append(result)
        
    return answer