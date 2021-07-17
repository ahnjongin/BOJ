m,n=map(int,input().split())

def prime(a):
    if a==1: return False

    for i in range(2,int(a**0.5+1)):
        if a%i==0:
            return False
    return True

for i in range(m,n+1):
    if prime(i):
        print(i)