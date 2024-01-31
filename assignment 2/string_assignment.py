#!/usr/bin/env python3

# Can use single or double quotes
name = "Cory"
occupation = 'Student'
tenure = 0.1
location = "Saddleback College"

results = f"\"{name}\" is a {occupation} at {location} "\
          f"\nand has been for over \'{tenure}\' years."

print(results)
