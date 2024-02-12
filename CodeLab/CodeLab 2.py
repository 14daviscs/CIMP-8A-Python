#! /usr/bin/env python3

# Greet player
print("BLACKJACK!")
print("Blackjack payout is 3:2")
print("Enter 'x' for bet to exit\n")

# Initialize variables
player_money = float(input("Starting money:   "))
print()
player_bet = input("Bet amount: ")
result = ''

# Loop until user exits
while result != 'x':
    result = input("Blackjack, win, push, or lose (b/w/p/l): ")
    if result == 'b':
        player_money = round(player_money + float(player_bet) * 1.5, 2)
        print(f"Money: {player_money}\n\nBet amount: {player_bet}")
    elif result == 'w':
        player_money = round(player_money + float(player_bet), 2)
        print(f"Money: {player_money}\n\nBet amount: {player_bet}")
    elif result == 'p':
        print(f"Money: {player_money}\n\nBet amount: {player_bet}")
    elif result == 'l':
        player_money = round(player_money - float(player_bet), 2)
        print(f"Money: {player_money}\n\nBet amount: {player_bet}")

# End program
print("\nGoodbye!")
