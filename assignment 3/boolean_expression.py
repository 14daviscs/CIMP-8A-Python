#!/usr/bin/env python3

x = 7

print(f"The value of x is {x}")

if x < 5:
    print(f"{x} is less than 5")

if x > 5:
    print(f"{x} is greater than 5")

if x == 5:
    print(f"{x} is equal to 5")

x = 3

print()
print(f"The value of x is {x}")

if x < 5:
    print(f"{x} is less than 5")
else:
    print(f"{x} is not less than 5")

x = 5

print()
print("The value of x is " + str(x))

if x < 5:
    print(f"{x} is less than 5")
elif x > 5:
    print(f"{x} is greater than 5")
else:
    print(f"{x} is equal to 5")