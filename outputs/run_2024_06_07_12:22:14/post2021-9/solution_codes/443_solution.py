for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    t = input().strip()

    if s.count('a') != t.count('a') or s.count('b') != t.count('b') or s.count('c') != t.count('c'):
        print("NO")
        continue

    diff = 0
    for i in range(n):
        if s[i] != t[i]:
            if i+1 < n and s[i:i+2] == 'ab' and t[i:i+2] == 'ba':
                diff += 1
                i += 1
            elif i+1 < n and s[i:i+2] == 'bc' and t[i:i+2] == 'cb':
                diff += 1
                i += 1
            else:
                diff += 2  # For any other case

    if diff % 2 == 0:
        print("YES")
    else:
        print("NO")