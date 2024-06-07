for _ in range(int(input())):
    s = input().strip()
    k = 0
    painted_chars = set()
    for char in s:
        if char not in painted_chars:
            k += 1
            painted_chars.add(char)
    print(k)