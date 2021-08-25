import sys
input=sys.stdin.readline
N,M=map(int,input().split())
L=list(map(int,input().split()))
sum_L=[0]
sum=0
for i in L:
    sum+=i
    sum_L.append(sum)
for i in range(M):
    a,b=map(int,input().split())
    print(sum_L[b]-sum_L[a-1])
