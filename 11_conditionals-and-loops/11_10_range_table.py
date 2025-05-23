# Read up on `range()` and additional options for `print()`.
# Then use a loop to print the following table to the console:
#
# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

# Loop through numbers 0 to 49.
for number in range(50):
    print(number, end= " ") # Instead of ending each print with a link break, end it with a space. 

# After every 10 numbers, print new line.
    if (number + 1) % 10 == 0: # Count how many numbers have printed so far. 
        print()