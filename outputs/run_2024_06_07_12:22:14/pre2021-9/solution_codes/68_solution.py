for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    flag = False

    for k in range(1, n+1):
        for i in range(n-k+1):
            subseq_a = a[i:i+k]
            if set(subseq_a).issubset(b):
                print("YES")
                print(k, " ".join(map(str, subseq_a)))
                flag = True
                break
        if flag:
            break

    if not flag:
        print("NO")