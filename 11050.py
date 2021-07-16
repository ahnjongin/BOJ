N, K = map(int,input().split())
on=1
down=1
for i in range(K):
    on*=N
    N-=1
for a in range(K):
    down*=K
    K-=1
print(on//down)
