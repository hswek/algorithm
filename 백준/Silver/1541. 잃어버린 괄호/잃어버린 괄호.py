import sys
string=sys.stdin.readline().rstrip().split('-')
result=sum(list(map(int,string[0].split('+'))))
for i in range(1,len(string)):
    a=sum(list(map(int,string[i].split('+'))))
    result-=a
    #print(a)
print(result)