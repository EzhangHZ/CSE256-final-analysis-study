def sum_of_digits(x):
    return sum(int(digit) for digit in str(x))

def count_interesting_numbers(n):
    count = 0
    for x in range(1, n+1):
        if sum_of_digits(x+1) < sum_of_digits(x):
            count += 1
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    result = count_interesting_numbers(n)
    print(result)