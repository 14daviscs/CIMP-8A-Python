#!/usr/bin/env python3

import random

ITEMS_FILENAME = "wizard_all_items.txt"
WIZARD_ITEMS_FILENAME = "wizard_items.txt"


def read_inventory_list():
    inventory = []
    with open(ITEMS_FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            inventory.append(line)
        return inventory


def read_wizard_items():
    inventory = []
    with open(WIZARD_ITEMS_FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            inventory.append(line)
        return inventory


def write_wizard_items(items):
    with open(WIZARD_ITEMS_FILENAME, "w") as file:
        for item in items:
            file.write(item + "\n")


def display_title():
    print("The Wizard Inventory program\n")


def wizard_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()


def walk(items):
    inventory = read_inventory_list()
    item = random.choice(inventory)
    print(f"While walking down a path, you see {item}")
    grab_it = input("Do you want to grab it? ").lower()

    if grab_it == "y":
        if len(items) < 4:
            items.append(item)
            write_wizard_items(items)
            print(f"{item} was added.\n")
        else:
            print("You can't carry any more items.\n")


def show_items(items):
    i = 1
    for item in items:
        print(f"{i}. {item}")
        i += 1

    print()


def drop_item(items):
    i = input("Number: ")
    i = int(i) - 1
    if 0 <= i < len(items):
        item = items.pop(i)
        write_wizard_items(items)
        print(f"{item} was dropped.\n")
    else:
        print("Invalid item number.\n")


def main():
    items = read_wizard_items()

    display_title()
    wizard_menu()

    while True:
        command = input("Command: ").lower()

        if command == "show":
            show_items(items)
        elif command == "walk":
            walk(items)
        elif command == "drop":
            drop_item(items)
        elif command == "exit":
            break
        else:
            print("Invalid command.\n")

    print("Bye!")


if __name__ == "__main__":
    main()
