def solution(today, terms, privacies):
    answer = []
    dd={}
    for i in terms:
        dd[i.split()[0]]=int(i.split()[1])
    t_y,t_m,t_d=today.split('.')
    t_y,t_m,t_d=int(t_y),int(t_m),int(t_d)
    for i in range(len(privacies)):
        s=privacies[i]
        when,what=s.split()
        
        y,m,d=when.split('.')
        y,m,d=int(y),int(m),int(d)
        m+=dd[what]
        y+=m//12
        m=m%12
        if m==0:
            y-=1
            m+=12
        #print(y,m,d,t_y,t_m,t_d)
        if y>t_y:
            continue
        elif y<t_y:
            answer.append(i+1)
        else:
            if m>t_m:
                continue
            elif m<t_m:
                answer.append(i+1)
            else:
                if d>t_d:
                    continue
                elif d<=t_d:
                    answer.append(i+1)
    return answer