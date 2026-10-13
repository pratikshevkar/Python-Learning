# 2. Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.

# Open and read all lines into a list
with open("info.txt", "r") as fp:
    lines = fp.readlines()

# 1. Print total number of lines
print(f"Total lines: {len(lines)}")

print(f"2nd Line: {lines[1].strip()}")

print(f"4th Line: {lines[3].strip()}")
