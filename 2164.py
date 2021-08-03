import sys
from collections import deque

a=int(sys.stdin.readline())
Q=deque([])
for i in range(a):
    Q.append(i+1)
while(len(Q)>1):
    Q.popleft()
    Q.append(Q.popleft())

print(Q.pop())