#!/usr/bin/env python3

x = 7

print("The value of x is " + str(x))

if x != 5:
    print(f"{x} is NOT equal to 5")
else:
    print(f"{x} is equal to 5")

print()

units = 14
gpa = 3.75

if units >= 12 and gpa >= 3.25:
    print("Eligible for Dean's list")
else:
    print("Not eligible for Dean's list")

print()
iPhone = input("Enter your iPhone version: ")

if iPhone == "10" or iPhone.upper() == "X":    # use upper case X here
    print("You have the best iPhone version")
else:
    print("You do not have the best iPhone version")
