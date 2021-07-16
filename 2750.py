a=int(input())
list=[]
for i in range(a):
    list.append(int(input()))
list2=sorted(list)

for j in range(len(list)):
    print(list2[j])