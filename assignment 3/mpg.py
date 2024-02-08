#!/usr/bin/env python3

print("Calculating Miles Per Gallon\n")
more = "y"
while more.lower() == "y":
    miles_driven = float(input("Enter miles driven:\t\t\t"))
    gallons_used = float(input("Enter gallons of gas used:\t"))

    # validate input
    if miles_driven <= 0 or gallons_used <= 0:
        print("Both entries must be greater than zero. Try again.\n")
        continue    # send flow back to the top

    mpg = round(miles_driven / gallons_used, 2)
    print(f"Miles Per Gallon:\t\t\t{mpg}\n")

    more = input("Continue? (y/n): ")
    print()

print("The program has ended")
