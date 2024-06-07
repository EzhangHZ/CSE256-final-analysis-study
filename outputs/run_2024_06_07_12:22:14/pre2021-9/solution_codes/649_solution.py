n = int(input())
s = input().strip()
swaps = 0

for i in range(n//2):
    if s[i] != s[n-i-1]:
        swaps += abs(i - (n-i-1))

print(swaps)