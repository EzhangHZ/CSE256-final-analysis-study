n, k = map(int, input().split())
s = input()

MOD = 998244353
factorial = [1] * (n+1)
for i in range(1, n+1):
    factorial[i] = (factorial[i-1] * i) % MOD

if k == 0:
    print(1)
else:
    count = 0
    for i in range(n - k + 1):
        if s[i:i+k].count('1') == k:
            ways_to_rearrange = factorial[k]
            ways_remaining = factorial[n-k] if k != n else 1
            count += (ways_to_rearrange * ways_remaining) % MOD
    print(count % MOD)