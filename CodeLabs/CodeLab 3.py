#! /usr/bin/env python3

import random


def welcome():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit\n")
    print()


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


def play_until_exit(player_money):
    while True:
        player_bet = input("Bet amount: ")
        if player_bet == 'x':
            break
        else:
            result = hand()

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


def main():
    welcome()
    player_money = float(input("Starting money:  "))
    print()
    play_until_exit(player_money)


main()


print("\nGoodbye!")
