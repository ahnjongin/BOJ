T=int(input())
sum=0
ti=list(map(int, input().split()))
ti.sort()
for i in range(T):
    for j in range(i+1):
        sum+=ti[j]
print(sum)