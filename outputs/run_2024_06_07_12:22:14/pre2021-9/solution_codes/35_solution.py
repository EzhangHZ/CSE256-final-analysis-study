for case in range(int(input())):
    x, y, z = map(int, input().split())
    if (x + y + z) % 2 != 0:
        print("NO")
        continue
    a = (x + y - z) // 2
    b = (x + z - y) // 2
    c = (y + z - x) // 2
    if a > 0 and b > 0 and c > 0:
        print("YES")
        print(f"{a} {b} {c}")
    else:
        print("NO")