#! /usr/bin/env python3

import random


# begin the program
def welcome():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit\n")
    print()


# determine results for each hand
def hand():
    result = random.randint(1, 100)
    if result <= 5:
        return "blackjack"
    elif result <= 42:
        return "win"
    elif result <= 51:
        return "push"
    else:
        return "lose"


# create a loop to be ended by the user
def play_until_exit(player_money):
    while True:
        player_bet = input("Bet Amount: ")

        # User exit and input validation for player's bet
        if player_bet == 'x':
            break
        elif int(player_bet) < 5:
            print("ERROR: The minimum bet is 5.")
            continue
        elif int(player_bet) > 1000:
            print("ERROR: The maximum bet is 1000.")
            continue
        elif int(player_bet) > player_money:
            print("ERROR: You don't have enough money for that bet.")
            continue
        else:
            result = hand()

        # Possible results due to random number generator
        if result == 'blackjack':
            player_money = round(player_money + float(player_bet) * 1.5, 2)
            print(f"BLACKJACK!")
        elif result == 'win':
            player_money = round(player_money + float(player_bet), 2)
            print("You won.")
        elif result == 'push':
            print("Push. You get your money back.")
        elif result == 'lose':
            player_money = round(player_money - float(player_bet), 2)
            print("You lost.")

        print(f"Money: {int(player_money)}\n")


# player_money is in main() so it persists through hands
def main():
    welcome()
    player_money = int(input("Starting money:  "))

    # Input validation for starting money
    while player_money < 5 or player_money > 10000:
        if int(player_money) < 5:
            print("ERROR: the minimum starting money is 5.")
        if int(player_money) > 10000:
            print("ERROR: The maximum starting money is 10,000.")
        player_money = float(input("Starting money:  "))

    print()
    play_until_exit(player_money)
    print("Goodbye!")


main()
