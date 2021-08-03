from collections import deque
a,b=map(int,input().split())
Q=deque([])
list_=[]
for i in range(a):
    Q.append(i+1)
while Q:
    for i in range(b-1):
        Q.append(Q[0])
        Q.popleft()
    chan=Q.popleft()
    list_.append(chan)
print('<', end='')
for i in range(len(list_)-1):
    print(list_[i],end=', ')
print("%d>"%list_[-1])