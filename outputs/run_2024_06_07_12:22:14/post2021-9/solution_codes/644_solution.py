n = int(input())
a = list(map(int, input().split()))

MOD = 10**9 + 7
ops_needed = 0
for i in range(n):
    ops_needed = (2 * ops_needed + a[i]) % MOD

print(ops_needed)