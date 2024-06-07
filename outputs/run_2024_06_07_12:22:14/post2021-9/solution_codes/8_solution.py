for _ in range(int(input())):
    n = int(input())
    s = input()
    
    if s[0] != 'T' and s[0] != 't':
        print("NO")
        continue
    
    counts = {c: s.count(c) for c in 'imur'}
    
    if all(count == 1 for count in counts.values()) and sum(counts.values()) == n:
        print("YES")
    else:
        print("NO")