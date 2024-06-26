def solution(n, words):
    answer = [0,0]
    idx=0
    word=words[0]
    d={}

    d[word]=True
    for i in words[1:]:
        if len(i)==1 or i[0]!=word[-1] or i in d:
            answer=[(idx+1)%n+1,(idx+1)//n+1] 
            break
        d[i]=True
        idx+=1
        word=i

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer