t=int(input())
stack=[]
list_=[]
count=1
temp=True
for i in range(t):
    num=int(input())
    while count <= num:
        stack.append(count)
        count+=1
        list_.append('+')
    if stack[-1]==num:
        stack.pop()
        list_.append('-')
    else:
        temp=False
if temp==False:
    print('NO')
else:
    for i in list_:
        print(i)