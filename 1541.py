a=input().split('-')
L=[]
for i in a:
    count=0
    b=i.split('+')
    for j in b:
        count+=int(j)
    L.append(count)
n=L[0]
for i in range(1,len(L)):
    n-=L[i]
print(n)