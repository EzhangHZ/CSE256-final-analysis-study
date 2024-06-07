def calculate_password_sequences(t):
    for _ in range(t):
        n = int(input())
        digits_not_used = set(map(int, input().split()))
        
        count = 0
        for d1 in range(10):
            for d2 in range(10):
                if d1 == d2 or d1 in digits_not_used or d2 in digits_not_used:
                    continue
                count += 1
        
        print(count * (count - 1))  # Number of permutations for the two different digits with repetitions

t = int(input())
calculate_password_sequences(t)