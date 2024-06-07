for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Check if the XOR of all elements in array is 0
    xor_sum = 0
    for num in a:
        xor_sum ^= num
    if xor_sum == 0:
        print("DRAW")
        continue
    
    # Calculate the XOR of all elements in array a
    if n % 2 == 0:
        print("LOSE")
    else:
        print("WIN")