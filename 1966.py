T=int(input())
for i in range(T):
    n,m= map(int, input().split())
    imp=list(map(int, input().split()))
    imp_=[0 for _ in range(n)]
    imp_[m]=1
    count=0
    while True:
        if imp[0]==max(imp):
            count+=1
            if imp_[0]==1:
                print(count)
                break
            else:
                del imp[0]
                del imp_[0]
        else:
            imp.append(imp[0])
            del imp[0]
            imp_.append(imp_[0])
            del imp_[0]