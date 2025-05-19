# Your hunger-meter currently only handles string input accurately.
# Replace your first `if` statement with a type check.
# If the value of `hunger` is not of the type `str`,
# print a message that reminds you to
# declare your hunger levels with a string.


hunger = 2

# Step 1: Check if hunger is not a string
if type(hunger) != str:
    print("Please declare your hunger level using a string.")
elif hunger == "big": # If hunger is a string and equals big, eat the pizza.
    print("Eat the pizza")
elif hunger == "small": # If hunger is a string and equals small, eat the apple.
    print("Eat the apple")
else:
    print("Don't eat anything")
