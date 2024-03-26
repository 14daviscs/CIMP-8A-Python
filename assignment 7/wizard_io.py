#!/usr/bin/env python3

WIZARD_FILE = "wizard_all_items.txt"


# Display the menu
def wizard_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()


# Add a new movie
def show(wizard_list):
    if len(wizard_list) == 0:
        print("You are not carrying anything.\n")
    else:
        for i, item in enumerate(wizard_list, start=1):
            print(f"{i}. {item}")
        print()


def grab(wizard_list):
    if len(wizard_list) < 4:
        item = input("Name: ")
        WIZARD_FILE.append(item)
        print(f"{item[0]} was added.\n")
    else:
        print("You can't carry any more items. Drop something first.\n")


def edit(wizard_list):
    item = input("Number: ")
    if int(item) <= len(wizard_list):
        wizard_list[int(item) - 1] = input("Update name: ")
        print(f"Item number {item} was updated.\n")
    else:
        print("Invalid item number.\n")


def drop(wizard_list):
    number = int(input("Number: "))
    if number < 1:
        print("You aren't carrying anything.\n")
    elif number > len(wizard_list):
        print("You aren't carrying that many items.\n")
    else:
        item = wizard_list.pop(number - 1)
        write_items(wizard_list)
        print(f"{item[0]} was deleted.\n")


def main():
    wizard_list = ["wooden staff", "wizard hat", "cloth shoes"]
    wizard_menu()

    while True:
        command = input("Command: ").lower()
        if command == "show":
            show(wizard_list)
        elif command == "grab":
            grab(wizard_list)
        elif command == "edit":
            edit(wizard_list)
        elif command == "drop":
            drop(wizard_list)
        elif command == "exit":
            break
        else:
            print("Invalid command.\n")

    print("Bye!")


if __name__ == "__main__":
    main()
