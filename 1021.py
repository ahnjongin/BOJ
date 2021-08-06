from collections import deque
n,m= map(int, input().split())
L=list(map(int, input().split()))

Q=deque([i for i in range(1,n+1)])
count=0
for j in L:
    while True:
        if Q[0]==j:
            Q.popleft()
            break
        else:
            if Q.index(j)<len(Q)/2:
                while Q[0] != j:
                    Q.append(Q.popleft())
                    count+=1
            else:
                while Q[0] != j:
                    Q.appendleft(Q.pop())
                    count+=1
print(count)