N=int(input())
M=1000-N
count=0
coin=[500,100,50,10,5,1]
for i in coin:
    count+=M//i
    M%=i
print(count)
