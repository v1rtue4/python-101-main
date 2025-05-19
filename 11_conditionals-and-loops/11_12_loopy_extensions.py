# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"

# Set a flag to track if it's a .pdf file.
is_pdf = False

# Loop through the filename
for i in range(len(filename)):
    # Look for start of the ".pdf" ending
    if filename[i] == ".":

        #Check if the next characters match "pdf"
        if i + 3 < len(filename):
            if (filename[i + 1] == "p" and # Check for pdf in specific file name.
                filename[i + 2] == "d" and
                filename[i + 3] == "f"):
                is_pdf = True # when found .pdf ending

# Display final result
if is_pdf:
    print("This is a PDF file.")