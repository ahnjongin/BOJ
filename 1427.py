a=int(input())
list=[]
for i in str(a):
    list.append(int(i))
list.sort(reverse=True)

for i in list:
    print(i,end='')

