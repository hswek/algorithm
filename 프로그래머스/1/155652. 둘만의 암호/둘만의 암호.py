def solution(s, skip, index):
    answer = ''
    for i in s:
        for j in range(index):
            while True:
                i=chr(ord(i)+1)
                if ord(i)==ord('z')+1:
                    i='a'
                if i not in skip:
                    break
        #print(answer,i)
        answer+=i
            
    return answer