#!/usr/bin/env python3

sport = "hockey"
city = "Anaheim"
team = ""

if sport == "baseball":
    if city.lower() == "anaheim":
        team = "Angels"
    else:
        team = "Dodgers"
elif sport == "hockey":
    if city.lower() == "anaheim":
        team = "Ducks"
    else:
        team = "Kings"

print(f"The {sport} team in {city} is the {team}")
