#! /usr/bin/env python3

name_first = str(input("Enter your first name: "))
name_last = str(input("Enter your last name: "))
birth_year = int(input("Enter the year you were born: "))
temp_pass = f"{name_first}*{birth_year}"

print()
print("Registration Form")
print()
print(f"First name:     {name_first}")
print(f"Last name:      {name_last}")
print(f"Birth year:     {birth_year}")
print()
print(f"Welcome, {name_first} {name_last}!")
print('Your registration is complete.')
print(f"Your temporary password is {temp_pass}")
