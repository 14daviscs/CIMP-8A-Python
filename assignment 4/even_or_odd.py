#!/usr/bin/env python3


def check_number(integer):
    if integer % 2 > 0:
        return "odd"
    else:
        return "even"


def main():
    user_number = int(input("Enter an integer: "))
    even_or_odd = check_number(user_number)

    if even_or_odd == "even":
        print("You have chosen an even number.\n")
    if even_or_odd == "odd":
        print("You have chosen an odd number.\n")

    restart = input("Check another number? (y/n): ")
    print()
    if restart == "y":
        main()


print("Even or Odd Checker\n")
main()
print("Bye!")
