N, M = map(int, input().split())

L=[]
def C():
    if len(L) == M:
        print(' '.join(map(str,L)))
        return

    for i in range(1, N+1):
        if i in L:
            continue
        L.append(i)
        C()
        L.pop()
C()