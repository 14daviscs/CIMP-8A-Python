#!/usr/bin/env python3

cars = ["Porsche", "Ford", "Mercedes"]

print("Unsorted List")
for car in cars:
    print(car)

print()
print("Sorted List - Ascending Order")
cars.sort()
for car in cars:
    print(car)

print()
print("Sorted List - Descending Order")
cars.sort(reverse=True)
for car in cars:
    print(car)

cars.append("BMW")
cars.append("Porsche")
print()
car = "Porsche"
print(f"The {car} occurs {cars.count(car)} times.")
