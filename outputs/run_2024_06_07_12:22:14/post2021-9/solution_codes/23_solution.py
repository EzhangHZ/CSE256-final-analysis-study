for _ in range(int(input())):
    n = int(input())
    # Calculate the height of the platforms
    h2 = n // 3
    h1 = h2 + (n % 3 > 0)
    h3 = h2 - (n % 3 == 2)
    
    print(h2, h1, h3)