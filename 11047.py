T,M=map(int,input().split())
list_=[int(input()) for i in range(T)]
list_.sort(reverse=True)
count=0
for i in list_:
    count+= M // i
    M%=i
print(count)