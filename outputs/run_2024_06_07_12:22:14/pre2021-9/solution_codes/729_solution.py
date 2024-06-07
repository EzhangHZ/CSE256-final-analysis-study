# Solution Code:

n = int(input())  # Read the total number of skyscrapers
h = list(map(int, input().split()))  # Read the heights of n skyscrapers and store them in a list h

count = 1  # Initialize the number of discrete jumps with the first jump from 1st to 2nd skyscraper

for i in range(n - 1):  # Loop through the first to second last skyscraper
    # Check the conditions for a discrete jump and increment count if met
    if max(h[i], h[i+1]) < min(h[i+1], h[i]):
        count += 1

print(count)  # Print the minimal amount of discrete jumps required

This code reads the heights of the skyscrapers, calculates the minimal number of discrete jumps Vasya needs to reach the last skyscraper, and prints the result.