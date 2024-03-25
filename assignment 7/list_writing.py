#!/usr/bin/env python3

OS = ["Mac OS", "Windows", "Android", "Linux"]

# Open the file in overwrite mode
with open("os.txt", "w") as file:
    # Write 1 element at a time
    for item in OS:
        # Note the \n, this will put each item on its own line in the file
        file.write(item + "\n")

new_os = []

# Open the file in read (default) mode
with open("os.txt") as file:
    # Read 1 element at a time
    for line in file:
        # We need to strip off the new line, or we will
        # get a blank line after each when we print
        line = line.replace("\n", "")
        new_os.append(line)

print(new_os)
