for _ in range(int(input())):
    s = input()
    x = int(input())
    n = len(s)
    w = ['0'] * n
    
    for i in range(n):
        if s[i] == '1':
            if i - x >= 0:
                w[i - x] = '1'
            if i + x < n:
                w[i + x] = '1'
    
    reconstructed_w = ''.join(w)
    
    if ''.join([s[j] if (j-x >= 0 and w[j-x] == '1') or (j+x < n and w[j+x] == '1') else '0' for j in range(n)]) == s:
        print(reconstructed_w)
    else:
        print(-1)