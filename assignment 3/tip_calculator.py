#!/usr/bin/env python3

print("Tip Calculator")
print()

# Get and print meal cost
initial_cost = float(input("Cost of meal: "))

# Determine tips
tip_15 = round(initial_cost * 0.15, 2)
tip_20 = round(initial_cost * 0.20, 2)
tip_25 = round(initial_cost * 0.25, 2)

# Print tip options
print()
print("15%")
print("Tip amount:   ", tip_15)
print("Total amount: ", round(initial_cost + tip_15, 2))
print()
print("20%")
print("Tip amount:   ", tip_20)
print("Total amount: ", round(initial_cost + tip_20, 2))
print()
print("25%")
print("Tip amount:   ", tip_25)
print("Total amount: ", round(initial_cost + tip_25, 2))
