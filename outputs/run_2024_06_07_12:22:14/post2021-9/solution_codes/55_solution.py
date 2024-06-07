for _ in range(int(input())):
    s = input()
    days = 1
    distinct_chars = set()
    
    for char in s:
        distinct_chars.add(char)
        if len(distinct_chars) > 3:
            days += 1
            distinct_chars.clear()
            distinct_chars.add(char)
    
    print(days)