n=int(input())
def fact(n):
    if n==-1:
        return 0
    if n==1 or n==0:
        return 1
    return fact(n-1)+fact(n-2)
print(fact(n-1))