a = int(input())
cnt = 1
cntplus = 6
road = 1
while a > cnt:
    road += 1
    cnt += cntplus
    cntplus += 6
print(road)