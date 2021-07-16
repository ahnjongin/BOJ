import math
A, B, V= map(int,input().split())
sum= (V-B)/(A-B)
print(math.ceil(sum))

