# Print out every prime number between 1 and 1000.

# Loop through numbers from 2 to 1000
for number in range(2, 1001):
    is_prime = True  # Prime

    # Check if number is divisible by any smaller number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break  # if False, stop checking

    # If it's still marked as prime, print
    if is_prime:
        print(number)
