#!/usr/bin/env python3
import os

# Open a file in write mode (overwrite)
file = open("hello.txt", "w")

# Write to the file
file.write("Hello World\n")
file.write("From Cory")    # use your name here

# Close the file
file.close()

# Read and print the entire file
print("\nThis will read and then print the entire file")
with open("hello.txt") as file:
    text = file.read()
    print(text)

# Read the entire file and print 1 line at a time
print("\nThis will read the entire file and then print 1 line at a time")
with open("hello.txt") as file:
    for line in file:
        print(line, end="")
    print()

# Read the entire file as a list
print("\nThis will read the entire file as a list and then print 1 list item at a time")
with open("hello.txt") as file:
    listItems = file.readlines()
    for item in listItems:
        print(item, end="")
    print()

# Read and print the file 1 line at a time
print("\nThis will read and print the file 1 line at a time")
with open("hello.txt") as file:
    line = file.readline()
    print(line, end="")
    line = file.readline()
    print(line, end="")
