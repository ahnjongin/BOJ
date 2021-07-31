t=int(input())
stack=[]
for i in range(t):
    count = 0
    a=input()
    stack=a
    for j in stack:
        if j=='(':
            count+=1
        elif j==')':
            count-=1
        if count<0:
            print('NO')
            break
    if count==0:
        print('YES')
    elif count>0:
        print('NO')
