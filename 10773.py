import sys

t=int(sys.stdin.readline())
stack=[]
for i in range(t):
    a=int(sys.stdin.readline())
    if a==0:
        stack.pop()
    else:
        stack.append(a)
print(sum(stack))

