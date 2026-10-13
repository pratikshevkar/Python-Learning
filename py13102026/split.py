# 3. Take a sentence from the user, split it into words, and store them in a list. Print the longest word.

# Take input
sentence = input("Enter a sentence: ")

# Split and store
words = sentence.split()

# Find and print the longest word
if words:
    longest_word = max(words, key=len)
    print(f"Longest word: {longest_word}")
else:
    print("No words were entered.")
