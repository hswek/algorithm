from collections import deque
def solution(s):
    answer = -1
    d=deque()
    for i in s:
        if len(d)==0:
            d.append(i)
        elif d[-1]==i:
            d.pop()
        else:
            d.append(i)
    if len(d)==0:
        return 1
    return 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer