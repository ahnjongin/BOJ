M= int(input())
N= int(input())
list=[]
for i in range(M, N+1):
    for a in range(2, i+1):
        if i==a:
            list.append(i)
        if i%a==0:
            break

if len(list)==0:
    print(-1)
else:
    print(sum(list))
    print(min(list))

