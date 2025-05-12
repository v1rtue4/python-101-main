# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

print(len(s)) # 77 characters, this will help with selecting range for texts [start:end]

print(s[57:-10]) # buttercups
print(s[57:-14]) # butter
print(s[5:9] + s[11] + s[-3]) # grapes
print(s[68:-4]) # flour
print(s[26:29] + s[-3]) # eggs