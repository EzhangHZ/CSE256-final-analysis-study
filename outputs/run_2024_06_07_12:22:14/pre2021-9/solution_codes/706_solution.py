# Solution Code:

for _ in range(int(input())):
    x, y, a, b = map(int, input().split())
    print(min(x//a, y//b))