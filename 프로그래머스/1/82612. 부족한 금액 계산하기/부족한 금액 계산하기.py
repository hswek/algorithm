def solution(price, money, count):
    answer = -1
    s=0
    for i in range(1,count+1):
        s+=i*price
    if s-money<0:
        money=s
    return s- money