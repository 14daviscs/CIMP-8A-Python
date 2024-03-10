#!/usr/bin/env python3

scores = [88, 91, 67, 82, 71, 84]
print(f"Test scores: {scores}")
print(f"The max score is: {max(scores)}")
print(f"The min score is: {min(scores)}")
print(f"The sum of all scores is: {sum(scores)}")


def passing_score(test_score):
    if test_score >= 70:
        return "passing"
    else:
        return "non-passing"


outcomes = map(passing_score, scores)  # This will return a map object
outcomes = list(outcomes)              # Convert the map object to a list


# Display the outcome for each score
print()
for score, outcome in zip(scores, outcomes):
    print(f"{score} is a {outcome} score")
