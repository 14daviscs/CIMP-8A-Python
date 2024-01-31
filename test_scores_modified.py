#! /usr/bin/env python3

print("The Test Scores Program")
print()
print("Enter test scores")
print("Enter 'Exit' to Quit")
print("=======================")

score_count = 0
score_total = 0

if input() == 'Exit':

else:
    score_total += input()
    score_count += 1

score_average = round(score_total / score_count)
print("=======================")

print("# of Scores: ", score_count)
print("Total score:   ", score_total)
print("Average score: ", score_average)
print()
print("Bye")
