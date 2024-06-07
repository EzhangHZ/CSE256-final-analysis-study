MOD = 998244353

for _ in range(int(input())):
    n = int(input())
    cells = input().strip()

    dp = [0] * n
    dp[0] = 1 if cells[0] == '0' else 0

    for i in range(1, n):
        if cells[i] == '1':
            dp[i] = 0
        else:
            if i >= 2 and cells[i-1] == '1':
                dp[i] += dp[i-2]
            if dp[i-1] > 0:
                dp[i] += dp[i-1]

        dp[i] %= MOD

    print(dp[-1])