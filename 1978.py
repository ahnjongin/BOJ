a=int(input())
b=map(int, input().split())
count=0
for i in b:
    for j in range(2,i+1):
        if j==i:
            count+=1
        if i%j==0:
            break

print(count)