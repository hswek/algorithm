def check_True(s):
    arr=[]    
    for i in s:
        if len(arr)==0:
            arr.append(i)
        elif arr[-1]=='(' and i==')':
            arr.pop()
        else:
            arr.append(i)
    if len(arr)==0:
        return True
    return False
def rec(p):
    global answer
    while True:
        if p=='':
            return ''
        tmp=''
        a=0
        b=0
        where=-1
        for i in range(len(p)):
            if p[i]=='(':
                a+=1
            else:
                b+=1
            if a==b:
                where=i
                break
        u=p[:where+1]
        v=p[where+1:]
        if check_True(u)==True:
            return u+rec(v)
            break
        else:
            tmp='('
            tmp+=rec(v)
            tmp+=')'
            u=u[1:]
            u=u[:-1]
            t=''
            for i in u:
                if i==')':
                    t+='('
                else:
                    t+=')'
            tmp+=t
            return tmp
def solution(p):
    global answer
    answer = rec(p)
    print(rec(p))
            
        
        
    return answer