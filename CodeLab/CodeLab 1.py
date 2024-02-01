#! /usr/bin/env python3

print("BLACKJACK!")
print("Blackjack payout is 3:2")
print()

player_start = float(input("Starting Money:    "))
player_bet = float(input("Bet Amount:          "))

blackjack = round(player_start + (player_bet * 1.5), 2)
win = round(player_start + player_bet, 2)
fold = round(player_start - player_bet, 2)

print()
print("ENDING MONEY FOR A...")
print("Blackjack:        ", blackjack)
print("Win:              ", win)
print("Push:             ", player_start)
print("Lose:             ", fold)
print()
print("See you next time!")
