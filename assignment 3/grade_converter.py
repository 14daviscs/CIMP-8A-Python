#!/usr/bin/env python3

# Initialize variables for number grade and letter grade
grade_letter = ""
grade_input = ""

print("Letter Grade Converter")
print()

# Create grade conversion loop
loop_check = "y"
while loop_check.lower() == "y":
    grade_input = input("Enter numerical grade: ")
    if int(grade_input) >= 88:
        grade_letter = "A"
        print("Letter_Grade: ", grade_letter)
    elif int(grade_input) >= 80:
        grade_letter = "B"
        print("Letter_Grade: ", grade_letter)
    elif int(grade_input) >= 67:
        grade_letter = "C"
        print("Letter_Grade: ", grade_letter)
    elif int(grade_input) >= 60:
        grade_letter = "D"
        print("Letter_Grade: ", grade_letter)
    else:
        grade_letter = "F"
        print(grade_letter)
    print()

    # Continue or finish loop
    loop_check = str(input("Continue? (y/n): "))
    print()

print()
print("Bye!")
