#!/usr/bin/env python3

# Open a file - read mode
file = open("test.txt", "r")

# The "r" is actually optional as it's the default
file = open("test.txt")

# Open a file - write mode (overwrite)
file = open("test.txt", "w")

# Open a file - write mode (append)
file = open("test.txt", "a")

# Write to the file
file.write("Hello World")

# Close the file
file.close()
