# Read all lines of input from a text file called "input.txt"
# Each line is a bank of batteries.
with open("input.txt") as f:
    banks = [line.strip() for line in f]

total = 0  # This will hold the sum of all maximum joltages

for bank in banks:
    max_value = 0  # Track the largest 2-digit number in this bank

    # Loop over all pairs of digits (i, j) with j after i
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form a two-digit number
            two_digit_number = int(bank[i] + bank[j])

            # Update max if this number is bigger
            if two_digit_number > max_value:
                max_value = two_digit_number

    # Add this bank's largest number to total
    total += max_value

# Print the final total output joltage
print("Total output joltage:", total)
