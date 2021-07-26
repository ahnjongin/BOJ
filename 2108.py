import sys
from collections import Counter
n=int(sys.stdin.readline())
list_=[]
for i in range(n):
    list_.append(int(sys.stdin.readline()))
list_.sort()
list_s=Counter(list_).most_common()
print(round(sum(list_)/len(list_)))
print(list_[len(list_)//2])
if len(list_s)>1:
    if list_s[0][1] == list_s[1][1]:
        print(list_s[1][0])
    else:
        print(list_s[0][0])
else:
    print(list_s[0][0])
print(list_[-1]-list_[0])