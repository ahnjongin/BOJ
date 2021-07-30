t=int(input())
for _ in range(t):
    a=int(input())
    b=int(input())
    list_=[i for i in range(1,b+1)]
    for _ in range(a):
        for j in range(1,b):
            list_[j]+=list_[j-1]
    print(list_[-1])
