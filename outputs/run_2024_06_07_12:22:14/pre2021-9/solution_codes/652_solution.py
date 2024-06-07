for _ in range(int(input())):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    days = 0
    balance = 0
    for i in range(n-1):
        balance = max(0, balance - b[i])
        balance += a[i]
        days += 1
        if balance >= c:
            break

    remaining_days = (c - balance + a[-1] - 1) // a[-1]
    days += remaining_days
    print(days)