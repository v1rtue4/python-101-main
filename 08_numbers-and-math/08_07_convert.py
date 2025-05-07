# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

# 1) Convert an int to a float
number = 4  # Currently an integer
converted_float = float(number)
print(converted_float)  # Output: 4.0

# 2) Convert a float to an integer
float_number = 4.45  # Float with decimal
converted_integer = int(float_number)
print(converted_integer)  # Output: 4 — decimal part (.45) is lost

# 3) Perform division using a float and an int
print(converted_float / converted_integer)  # 4.0 / 4 = 1.0

# 4) Use two variables to perform a multiplication
print(converted_integer * converted_float)  # 4 * 4.0 = 16.0