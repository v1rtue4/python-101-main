# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

# Utilize String Method str.endswith(), replace filenames
print(file_1.endswith("pdf"))  # Correct
print(file_2.endswith("pdf"))  # False
print(file_3.endswith("pdf"))  # False
print(file_4.endswith("pdf"))  # Correct
