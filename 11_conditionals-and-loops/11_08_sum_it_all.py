# Using a loop, sum all numbers from the `start` to the `stop` number.
# The sequence should consist only of integers from 1 to 100.
# The output of your calculation should look like this:
#
#      The sum is: 5050

start = 1
stop = 100

total = 0  # Start with zero

# Loop from 1 to 100
for number in range(start, stop + 1):
    total += number  # Add current number to the total

# After the loop, print the result
print("The sum is:", total)
