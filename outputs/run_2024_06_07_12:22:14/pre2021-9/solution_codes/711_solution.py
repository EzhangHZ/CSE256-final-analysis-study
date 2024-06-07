# Solution Code:

n = int(input())
a = list(map(int, input().split()))

count_0 = count_1 = 0

for i in range(n):
    if i % 2 == 0: # Assign color based on index parity
        if a[i] % 2 == 0:
            count_0 += 1
    else:
        if a[i] % 2 != 0:
            count_1 += 1

print(min(count_0 + (n + 1) // 2 - (count_0 > n // 2), count_1 + n // 2 - count_1))