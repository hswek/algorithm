def solution(s, n):
    answer = ''
    for i in s:
        if i==' ':
            answer+=' '
            continue
        if i==i.lower():
            i=chr(ord(i)+n)
            if ord(i)>ord('z'):
                i=chr(ord(i)-ord('z')+ord('a')-1)
            answer+=i
        if i==i.upper():
            i=chr(ord(i)+n)
            if ord(i)>ord('Z'):
                i=chr(ord(i)-(ord('Z')-ord('A'))-1)
            answer+=i
    return answer