# Solution Code:

for _ in range(int(input())):
    n, m = map(int, input().split())
    max_rounded_price = n * m
    max_rounds = 0
    for k in range(1, m+1):
        potential_price = n * k
        trailing_zeros = 0
        while potential_price % 10 == 0:
            trailing_zeros += 1
            potential_price //= 10
        if trailing_zeros > max_rounds:
            max_rounds = trailing_zeros
            max_rounded_price = n * k
    print(max_rounded_price)