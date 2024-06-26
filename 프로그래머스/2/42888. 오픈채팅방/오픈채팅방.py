def solution(records):
    answer = []
    d=  {}
    for record in records:
        arr=record.split()
        if arr[0]=='Change':
            d[arr[1]]=arr[2]
        if arr[0]=='Enter':
            d[arr[1]]=arr[2]
    for record in records:
        arr=record.split()
        if arr[0]=='Enter':
            answer.append(d[arr[1]]+'님이 들어왔습니다.')
        if arr[0]=='Leave':
            answer.append(d[arr[1]]+'님이 나갔습니다.')
    return answer