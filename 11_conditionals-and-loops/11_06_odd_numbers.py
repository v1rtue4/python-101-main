# Using a `for` loop, print out all odd numbers from 1 to 100.

# Loop from 1 to 100
for number in range(1, 101):
    # Check odd number
    if number % 2 != 0:
        print(number)