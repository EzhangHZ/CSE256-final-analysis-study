# Function to calculate factorial using modulo
def factorial(n, m):
    fact = 1
    for i in range(1, n + 1):
        fact = (fact * i) % m
    return fact

# Function to calculate modular inverse using extended Euclidean algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Main code
n, m = map(int, input().split())

# Calculate initial sum of happiness value
happiness = 0
inv_n_fact = mod_inverse(factorial(n, m), m)
for i in range(1, n + 1):
    happiness = (happiness + i * (n - i + 1) * inv_n_fact) % m

print(happiness)