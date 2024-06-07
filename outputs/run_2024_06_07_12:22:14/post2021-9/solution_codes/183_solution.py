for _ in range(int(input())):
    n, m = map(int, input().split())
    
    if (n == 1 and m == 1):
        print(0)
    elif n % 2 == 0 or m % 2 == 0:
        print(1)
    else:
        print(2 * (n // 2) + (m % 2))