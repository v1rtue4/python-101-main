# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

n = 20 # Start with this number

# Loop from 1 to n.
for number in range(1, n + 1): # Start at 1, go up to 20 and repeat everything inside loop once for each number.
    
    # Check if divisible by both 3 and 5 first.
    if number % 3 == 0 and number % 5 == 0: # % modulus gives the remainder, to divide evenly.
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)