def solution(s):
    answer = 0
    if s[0]=='+':
        s=s[1:]
        return int(s)
    if s[0]=='-':
        s=s[1:]
        return -1* (int(s))
    return int(s)
    return answer