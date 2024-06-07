for case in range(int(input())):
    n, w, h = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n-1):
        if a[i] + w >= a[i+1] - w or b[i] + h >= b[i+1] - h:
            print("NO")
            break
    else:
        a.sort()
        b.sort()
        shift_possible = True
        for i in range(n):
            if a[i] - w > b[i] - h or a[i] + w < b[i] + h:
                shift_possible = False
                break
        if shift_possible:
            print("YES")
        else:
            print("NO")