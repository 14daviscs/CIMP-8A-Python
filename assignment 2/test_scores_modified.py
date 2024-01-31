#! /usr/bin/env python3

print("The Test Scores Program")
print()
print("Enter test score")
print("Enter 'exit' to Quit")
print("=" * 20)

score_count = 0
score_total = 0

while True:
    score = input("Enter test score: ")

    if score == 'exit':
        break

    score_total += int(score)
    score_count += 1

score_average = round(score_total / score_count)

print("=" * 20)
print(f"# of Scores:     {score_count}")
print(f"Total Score:   {score_total}")
print(f"Average Score:  {score_average}")
print()
print("See you next time!")
