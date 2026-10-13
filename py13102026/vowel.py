# 1. Write a program to read a file and count how many vowels are present in its content.

# read the file
with open("info.txt", "r", encoding="utf-8") as file:
    content = file.read()

    count = 0

# check each word if its vowel then increase count
    for i in content:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            count = count +1
print(f"total vowels are {count}")