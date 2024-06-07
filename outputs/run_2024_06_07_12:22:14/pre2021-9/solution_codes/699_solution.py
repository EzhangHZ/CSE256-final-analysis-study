n = int(input())
a = list(map(int, input().split()))
length = 0

i = 0
while i < n-1:
    if a[i] == a[i+1]:
        a[i] += 1
        length += 1
        a.pop(i+1)
        n -= 1
        if i > 0:
            i -= 1
    else:
        i += 1

print(length + 1)