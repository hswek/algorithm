def solution(numbers):
    answer = []
    for num in numbers:
        if num%2==0:
            answer.append(num+1)
        else:
            a=1
            while True:
                where=1<<a
                
                if (where & num)==0:
                    #print( num | (1<<a),(1<<(a-1)))
                    num= (num | (1<<a)) -  (1<<(a-1))
                    answer.append(num)
                    break
                a+=1
    return answer