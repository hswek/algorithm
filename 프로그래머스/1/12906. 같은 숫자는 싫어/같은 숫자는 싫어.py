from collections import deque
def solution(arr):
    answer = deque([])
    for i in arr:
        if len(answer)==0:
            answer.append(i)
        elif answer[-1]!=i:
            answer.append(i)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return list(answer)