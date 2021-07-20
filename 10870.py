def fi(n):
    if n<=1:
        return n
    return fi(n-1)+fi(n-2)

n=int(input())
print(fi(n))


#반복문
#n=int(input())
#list=[0,1,]
#for i in range(2,n+1):
#    sum=list[i-1]+list[i-2]
#    list.append(sum)
#print(list[n])

