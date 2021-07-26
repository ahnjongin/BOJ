import sys
n=int(sys.stdin.readline())
list_=[]
for i in range(n):
    list_.append(list(map(int,sys.stdin.readline().split())))
list_.sort(key=lambda x:(x[1],x[0]))

for i in list_:
    print(i[0],i[1])