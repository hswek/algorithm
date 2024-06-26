from collections import deque
class linked_list:
    def __init__(self,num):
        self.num=num
        self.child=None
        self.parent=None
    def link_parent(self,p):
        self.parent=p
    def link_child(self,c):
        self.child=c
    def delete(self,stack,d):
        d[self.num]=False
        stack.appendleft(self.num)
        if self.parent != None:
            self.parent.child=self.child
        if self.child !=None:
            self.child.parent=self.parent
        if self.child!= None:
            return self.child
        return self.parent
    def next_node(self):
        return self.child
    def prev_node(self):
        return self.parent
def solution(n, k, cmd):
    answer = ''
    d={}
    is_true={}
    for i in range(n):
        tmp=linked_list(i)
        d[i]=tmp
        is_true[i]=True
        if i!=0:
            tmp.link_parent(d[i-1])
            d[i-1].link_child(tmp)
    now=d[k]
    stack=deque()
    for c in cmd:
        if now==None:
            print(-1)
            break
        if c[0]=='D':
            for i in range(int(c[2:])):
                now=now.next_node()        
        elif c[0]=='U':
            for i in range(int(c[2:])):
                now=now.prev_node()   
        elif c[0]=='C':
            now=now.delete(stack,is_true)
        elif c[0]=='Z':
            where=stack.popleft()
            is_true[where]=True  
            tmp=d[where]
            if tmp.parent is not None:
                tmp.parent.child=tmp
            if tmp.child is not None:
                tmp.child.parent=tmp
    for i in range(n):
        if is_true[i]==True:
            answer+='O'
        else:
            answer+='X'
                
    return answer