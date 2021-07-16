a=int(input())
result=0
for i in range(1, a+1):
    b=list(map(int, str(i)))
    result = i+sum(b)
    if result ==a:
        print(i)
        break
    if i==a:
        print("0")


