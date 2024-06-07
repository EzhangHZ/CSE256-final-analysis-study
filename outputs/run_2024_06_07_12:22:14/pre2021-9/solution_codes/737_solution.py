n, M = map(int, input().split())

dp = [0] * n
dp[0] = 1
dp[1] = 1

for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2]) % M

total_ways = (dp[n-1] + dp[n-2]) % M

print(total_ways)