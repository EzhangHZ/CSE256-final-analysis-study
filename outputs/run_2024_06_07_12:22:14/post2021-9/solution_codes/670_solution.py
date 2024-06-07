MOD = 10**9 + 7

def count_occurrences(s, t):
    n, m = len(s), len(t)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(m):
            if i + 1 < n and s[i] == t[j]:
                dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
            dp[i + 1] = dp[i + 1] % MOD
    return dp[n]

for _ in range(int(input())):
    s = input().strip()
    t = input().strip()

    moves = 0
    while s.find(t) != -1:
        s = s[:s.find(t)] + '.' + s[s.find(t)+len(t):]
        moves += 1

    opt_sequences = count_occurrences(s, t)

    print(moves, opt_sequences)