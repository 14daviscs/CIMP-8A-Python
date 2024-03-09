#!/usr/bin/env python3

# Create a list of "Office" characters
office = ["Dwight", "Michael", "Jim"]
# Update the second item in the list
office[1] = "Andy"
# Add a new item to the end of the list
office.append("Pam")
# Insert a new item into the 2nd position of the list
office.insert(1, "Stanley")
# Remove an item from the list by value
office.remove("Andy")
# Remove an item from the list by index
removed_character = office.pop()  # This will remove the last item in the list
# Remove an item from the list by index
character = office.pop(1)

# Display the characters in the "Office" list
print("List of Office characters:")
for character in office:
    print(character)

# Display the second and last items in the list
print()
print(f"The second item in the list is: {office[1]}")
print(f"The last item in the list is: {office[-1]}")

print(f"{removed_character} was deleted from the list")

# Determine if an item is in the list
character = "Jim"
if character in office:
    print(f"{character} is in the office character list")

# Display the number of items in the list
print(f"There are {len(office)} characters in the office list")
