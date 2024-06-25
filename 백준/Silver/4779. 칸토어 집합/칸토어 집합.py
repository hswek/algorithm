import sys
def kan(n,start,end):
    if n==0:
        print('-',end='')
        return
    kan(n-1,start,start+3**(n-1)-1)
    print(' '*3**(n-1),end='')
    kan(n-1,start+3**(n-1)*2,end)
while True:
    n=sys.stdin.readline().rstrip()
    if n=='':
        break
    n=int(n)
    kan(n,1,3**n)
    print('')