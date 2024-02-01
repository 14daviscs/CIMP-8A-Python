#! /usr/bin/env python3

print("BLACK JACK")
print("Blackjack payout is 3:2")
print()

player_start = float(input("Starting money:   "))
player_bet = float(input("Bet amount:       "))

blackjack = round(player_start + (player_bet * 1.5), 2)
win = round(player_start + player_bet, 2)
lose = round(player_start - player_bet, 2)

print()
print("ENDING MONEY FOR A...")
print("Blackjack:       ", blackjack)
print("Win:             ", win)
print("Push:            ", player_start)
print("Lose:            ", lose)
print()
print("Bye!")
