# Read input values
n = int(input())
beauty_values = list(map(int, input().split()))

# Initialize variables
max_beauty = 0
current_beauty = beauty_values[0]

# Loop through cities to find optimal journey plan
for i in range(1, n):
    if beauty_values[i] - i == current_beauty:
        current_beauty = beauty_values[i]
    else:
        max_beauty += current_beauty
        current_beauty = beauty_values[i]

# Include the beauty value of the last city in the journey
max_beauty += current_beauty

# Print the maximum beauty value of the journey
print(max_beauty)