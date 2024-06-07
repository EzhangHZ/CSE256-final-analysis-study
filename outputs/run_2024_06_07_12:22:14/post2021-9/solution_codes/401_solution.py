for _ in range(int(input())):
    k, x = map(int, input().split())
    
    total_emotes = k * (k + 1) // 2
    
    if total_emotes >= x:
        print(k)
        continue
    
    messages_sent = 0
    current_emotes = 0
    
    for i in range(1, 2*k):
        current_emotes += i
        if current_emotes >= x:
            print(i)
            break
        messages_sent += 1
    else:
        print(2*k-1)