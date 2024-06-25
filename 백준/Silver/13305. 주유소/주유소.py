import sys
n=int(input())
road_length=list(map(int,sys.stdin.readline().rstrip().split()))
oil_price=list(map(int,sys.stdin.readline().rstrip().split()))
price_sum=0
i=0
while(i<n-1):
    now=i
    while now<(n-1) and oil_price[i]<=oil_price[now]:
        price_sum+=road_length[now]*oil_price[i]
        now+=1
    i=now
print(price_sum)