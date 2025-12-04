C, N = map(int,input().split())
c_list  = []
for _ in range(N):
    b, c = map(int, input().split())
    c_list.append([b, c])

MAX = 100 * 1000
dp = [0] * (MAX + 1)
for b,c in c_list:
    for money in range(b, MAX+1):
        dp[money] = max(dp[money], dp[money-b] + c)
for money in range(MAX+1):
    if dp[money] >= C:
        print(money)
        break