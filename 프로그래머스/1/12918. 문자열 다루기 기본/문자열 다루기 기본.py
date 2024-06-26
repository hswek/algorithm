def solution(s):
    answer = True
    if not (len(s)==4 or len(s)==6):
        return False
    try:
        s=int(s)
        return True
    except:
        return False
    return answer