#! /usr/bin/env python3
import random

print("BLACK JACK")
print("Blackjack payout is 3:2")
print()
print("Starting money:   100")
print("Bet amount:       5")
print()
print("ENDING MONEY FOR A...")
print("Blackjack:        107.5")
print("Win:              105.0")
print("Push:             100.0")
print("Lose:             95.0")
print()
print("Bye!")

playerStart = input(int() or float())
playerBet = input(int() or float())
playerEnd = 0

def blackjack():
    playerEnd = round(playerStart + playerBet * 1.5)
    return playerEnd
def win():
    playerEnd = round(playerStart + playerBet)
    return playerEnd
def push():
    playerEnd = round(playerStart * 1)
    return playerEnd
def lose():
    playerEnd = round(playerStart - playerBet)
    return playerEnd

def play():
    random(blackjack(), win(), push(), lose())
    return print(f"You now have {playerEnd} money. Thanks for playing!")
