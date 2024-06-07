for _ in range(int(input())):
    x = input().strip()
    k = int(input())

    while k > 0:
        min_index = 0
        for i in range(1, len(x)):
            if int(x[i]) < int(x[min_index]):
                min_index = i
        
        x = x[:min_index] + x[min_index+1:]
        if x[0] == '0':
            x = x.lstrip('0')

        k -= 1

    if x == "":
        print(0)
    else:
        print(int(x))