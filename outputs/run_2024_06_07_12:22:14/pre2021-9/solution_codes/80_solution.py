# Solution Code:

for _ in range(int(input())):
    k = int(input())
    if k == 100:
        print(1)
        continue
    if k <= 50:
        print(100 - k)
    else:
        print(k)