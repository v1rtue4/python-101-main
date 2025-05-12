# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

print(len(word)) # Number of characters in word variable

# we see trees - identify letters, spaces, and words
print(word[1:3]) # We
print(word[-1]) # space
print(word[-2]) # s
print(word[2:4]) # ee
print(word[0]) #t
print(word[-3]) #r
print(word[2:4]) #ee
print(word[1:3] + word[-1] + word[-2] + word[2:4] + word[-1] + word[0] + word[-3] + word[2:4] + word[-2]) # concate - we see trees 
