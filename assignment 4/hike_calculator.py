#!/usr/bin/env python3


def calculate_feet(miles):
    feet_walked = int(round(miles * 5280, 2))
    return feet_walked


def main():
    print("Hike Calculator\n")
    miles_walked = float(input("How many miles did you walk? "))
    feet_walked = calculate_feet(miles_walked)
    print(f"You walked {feet_walked} feet.")


main()
