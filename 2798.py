n,m=map(int,input().split())
card=list(map(int,input().split()))
sum=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum2=card[i]+card[j]+card[k]
            if sum2<=m:
                sum.append(sum2)
print(max(sum))
