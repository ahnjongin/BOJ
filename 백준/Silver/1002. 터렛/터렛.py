import math
t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print("-1")
        else:
            print("0")
    else:
        if abs(r1 - r2) < dis < (r1 + r2):
            print ("2")
        elif (r1 + r2) == dis or dis == abs(r1 - r2):
            print("1")
        else:
            print("0")

