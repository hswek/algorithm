def to_sec(t):
    h,m,s=t.split(':')
    h=int(h)
    m=int(m)
    ss=int(float(s)*1000)
    return (3600*h+60*m)*1000+ss
def to_ss(t):
    t=t[:-1]
    t=int(float(t)*1000)
    return t
def solution(lines):
    answer = 0
    for l in range(len(lines)):
        a,t,h=lines[l].split()
        end=to_sec(t)
        h=to_ss(h)
        start=max(0,end-int(h)+1)
        result=1
        for l2 in range(len(lines)):
            if l==l2:
                continue
            a,t,h=lines[l2].split()
            end2=to_sec(t)
            h=to_ss(h)
            #print(end2,h)
            start2=max(0,end2-int(h)+1) 
            if not (end>end2 or end+999<start2):
                #print(end,end+999,start2,end2,end>end2,end+999<start)
                result+=1
        answer=max(answer,result)
    return answer