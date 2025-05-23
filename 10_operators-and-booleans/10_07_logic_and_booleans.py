# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#
#   do two wrongs make a right?
# 
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)

wrong = False
right = True

# Use all three logical operators in one line
# Combining wrong, right, and using not to invert one of them
result = (wrong and not wrong) or right

# Display the result
print(result)