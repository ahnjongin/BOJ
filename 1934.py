def gcd(A, B):
    if (A%B) == 0:
    	return B
    if B == 0:
        return A
    else:
        return gcd(B, A%B)
T=int(input())
for i in range(T):
    A,B= map(int, input().split())
    print(int(A*B/gcd(A,B)))