n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

MOD = 998244353

ways = 1

j = 0
for i in range(n):
    if a[i] == b[j]:
        ways *= (i-j)
        j += 1

print(ways % MOD if j == m else 0)