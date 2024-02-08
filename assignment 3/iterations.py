#!/usr/bin/env python3

choice = "y"
while choice.lower() == "y":
    print("Hello!")
    choice = input("Say Hello again (y/n): ")

print()

counter = 0
print("while Loop is < 5")
while counter < 5:
    print(counter, end = " ")
    counter += 1
print("\nThe loop has ended")

print()

print("for Loop range 5")
for i in range(5):
    print(i, end = " ")
    counter += 1
print("\nThe loop has ended")

print()

print("for Loop range 5 to 10")
for i in range(5, 10):
    print(i, end = " ")
    counter += 1
print("\nThe loop has ended")

print()

print("for Loop range 0 to 10, skip 2")
for i in range(0, 10, 2):
    print(i, end = " ")
    counter += 1
print("\nThe loop has ended")

print()

print("Enter 'exit' when you\'re done.")
while True:
    data = input("Enter an integer to square: ")
    if data == "exit":
        break
    i = int(data)
    print(f"{i} squared is {i * i}\n")
print("The program has ended")

print("Good Bye!")
