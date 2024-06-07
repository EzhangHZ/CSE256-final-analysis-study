for _ in range(int(input())):
    s = input().strip()
    
    if s[0] == s[-1]:
        print("a " + s[1:] + " b")
    else:
        count_b = s.count('b')
        
        if count_b % 2 == 0:
            a = 'a' + 'b' * (count_b // 2)
            b = s[len(a):-count_b // 2]
            c = 'b' * (count_b // 2)
            print(a + " " + b + " " + c)
        else:
            print(":(")