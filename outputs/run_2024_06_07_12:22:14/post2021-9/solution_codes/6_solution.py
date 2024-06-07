for _ in range(int(input())):
    s = input().strip()
    if len(s) % 2 != 0:
        print("NO")
        continue
    square_string = s + s
    if s in square_string:
        print("YES")
    else:
        print("NO")