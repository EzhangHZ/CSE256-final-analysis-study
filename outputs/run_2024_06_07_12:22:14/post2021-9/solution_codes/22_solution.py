t = int(input())  # number of test cases

for _ in range(t):
    expr = input()
    a, b = map(int, expr.split('+'))
    result = a + b
    print(result)