import sys

n=int(sys.stdin.readline())
list_=list(map(int,sys.stdin.readline().split()))

list_s=sorted(set(list_))
list_s={list_s[i]:i for i in range(len(list_s))}

print(*[list_s[i] for i in list_])