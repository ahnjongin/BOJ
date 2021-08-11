T=int(input())
distance=list(map(int,input().split()))
oil=list(map(int,input().split()))
sum=distance[0]*oil[0]
m=oil[0]
value=0
for i in range(1,T-1):
    if oil[i] < m:
        sum+= m*value
        value=distance[i]
        m=oil[i]
    else:
        value += distance[i]
    if i == T-2:
        sum += m*value
print(sum)