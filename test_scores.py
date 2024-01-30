#! /usr/bin/env python3

print("The Test Scores Program")
print()
print("Enter three test scores")
print("=======================")

scoreOne = int(input("Enter test score: "))
scoreTwo = int(input("Enter test score: "))
scoreThree = int(input("Enter test score: "))
scoreTotal = (scoreOne + scoreTwo + scoreThree)
scoreAverage = round(scoreTotal / 3)
print("=======================")

print("Total score:   ", scoreTotal)
print("Average score: ", scoreAverage)
print()
print("Bye")
