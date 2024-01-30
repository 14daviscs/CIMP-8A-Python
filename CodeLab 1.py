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

playerStart = 100
playerBet = 5
playerEnd = 0

blackjack = round(playerStart + playerBet * 1.5)
win = round(playerStart + playerBet)
push = round(playerStart * 1)
lose = round(playerStart - playerBet)

def play():
    random.choice(blackjack, win, push, lose)
    return print(f"You now have {playerEnd}. Thanks for playing!")
