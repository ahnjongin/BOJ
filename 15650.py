N, M = map(int, input().split())

L=[]
def C(start):
    if len(L) == M:
        print(' '.join(map(str,L)))
        return

    for i in range(start, N+1):
        L.append(i)
        C(i+1)
        L.pop()
C(1)