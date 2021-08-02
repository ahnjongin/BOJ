import sys
from collections import deque
t=int(sys.stdin.readline())
Q=deque([])
for _ in range(t):
    a=sys.stdin.readline().split()
    if a[0]=='push':
        Q.append(a[1])
    elif a[0]=='pop':
        if not Q:
            print(-1)
        else:
            print(Q.popleft())
    elif a[0]=='size':
        print(len(Q))
    elif a[0]=='empty':
        if not Q:
            print(1)
        else:
            print(0)
    elif a[0]=='front':
        if not Q:
            print(-1)
        else:
            print(Q[0])
    elif a[0]=='back':
        if not Q:
            print(-1)
        else:
            print(Q[-1])
