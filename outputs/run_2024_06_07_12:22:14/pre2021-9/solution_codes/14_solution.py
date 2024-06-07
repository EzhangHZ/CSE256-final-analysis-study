t = int(input())  # Read the number of test cases

# Loop through each test case
for _ in range(t):
    x = int(input())  # Read the apartment number

    num_digits = len(str(x))  # Calculate the number of digits in the apartment number
    total_digits = 0  # Initialize the total number of keypresses

    total_digits += 10 * (num_digits - 1)  # Adding keypresses for numbers with fewer digits

    for i in range(1, 10):
        total_digits += i

        if str(i) * num_digits == str(x):  # Check if the apartment number consists of the same digit
            break

    print(total_digits)  # Print the total number of digits our character pressed in total