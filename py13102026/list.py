# 4. Read a file, split its content into words, and store them in a list.
# Print the total number of words.
# Print all unique words.

# Read the file and split content into a list of words
with open("info.txt", "r") as fp:
    content = fp.read()
    words = content.split()

# Extract unique words using a set
unique_words = set(words)

# results
print(f"Total number of words: {len(words)}")
print(f"Total number of unique words: {len(unique_words)}")
print("Unique words list:", list(unique_words))
