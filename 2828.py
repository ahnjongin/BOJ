N,M=map(int,input().split())
T=int(input())
start=1
end=M
dis=0
for i in range(T):
    i=int(input())
    if i<start:
        dis+=(start-i)
        start=i
        end=i+M-1
    elif i > end:
        dis += (i - end)
        end = i
        start = end - M +1
print(dis)


