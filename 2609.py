a,b= map(int,input().split())
if a>b:
    a,b=b,a
so=0
if a>0:
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            so = i
else:
    exit

print(1 if so==0 else so)
print(a*b if so==0 else a*b//so)