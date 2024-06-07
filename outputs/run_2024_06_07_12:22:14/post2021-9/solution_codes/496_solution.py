n = int(input())  # Read the number of rounds
s = input()  # Read the symbols appearing in each round

q = int(input())  # Read the number of controllers

# Loop through each controller
for _ in range(q):
    a, b = map(int, input().split())  # Read the numbers on the buttons of the controller

    score = 0  # Initialize the score to 0

    # Loop through each round
    for i in range(n):
        if s[i] == '+':
            score += a if a <= b else b  # Increase score by the smaller number
        else:
            score -= a if a <= b else b  # Decrease score by the smaller number

    # Check if the final score is 0 and print the result
    if score == 0:
        print("YES")
    else:
        print("NO")