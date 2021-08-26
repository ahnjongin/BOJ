T=int(input())
L=[]
for i in range(T):
    s,e=map(int,input().split())
    L.append([s,e])
L=sorted(L,key=lambda a: a[0])
L=sorted(L,key=lambda a: a[1])
last=0
count=0
for i,j in L:
    if i >= last:
        count+=1
        last=j
print(count)