def solution(new_id):
    answer = ''
    s=new_id.lower()
    tmp=''
    for i in s:
        if i.isalpha() or i.isdigit() or i=='-' or i=='_' or i=='.':
            tmp+=i
    s=tmp
    prev='|'
    tmp=''
    for i in s:
        if prev=='|':
            prev=i
            tmp+=i
            continue
        if prev=='.' and i=='.':
            continue
        prev=i
        tmp+=i
    s=tmp
    if len(s)>=1 and s[0]=='.':
        if len(s)==1:
            s=''
        else:
            s=s[1:]
            
    if len(s)>=1 and s[-1]=='.':
        s=s[:-1]
        
    if s=='':
        s='a'
    if len(s)>=16:
        s=s[:15]

    if len(s)>=1 and s[-1]=='.':
        s=s[:-1]

    prev='|'
    tmp=''
    for i in s:
        if prev=='|':
            prev=i
            tmp+=i
            continue
        if prev=='.' and i=='.':
            continue
        prev=i
        tmp+=i
    s=tmp
    while len(s)<3:
        s=s+s[-1]
    return s