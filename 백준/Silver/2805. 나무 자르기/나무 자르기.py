import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(trees)
result = 0

while left <= right:
    mid = (left + right) // 2 
    cut = sum(tree - mid for tree in trees if tree > mid) 

    if cut >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1 

print(result)