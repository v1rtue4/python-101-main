# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution = ""

# For each character in secret, if it's a letter, add it to solution.
for char in secret:
    if char.isalpha():
        solution += char

# Display result
print(solution)