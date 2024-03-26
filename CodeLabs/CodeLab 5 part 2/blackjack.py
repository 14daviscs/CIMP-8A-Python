#! /usr/bin/env python3

import deck


# begin the program
def display_header():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit\n")
    print()


# determine results for each hand
def get_starting_amount():
    while True:
        player_money = float(input("Starting player money: "))
        if 5 < player_money <= 10000:
            print()
            return player_money
        else:
            print("Invalid amount. Must be between 5 and 10,000. Please try again.")


def get_bet_amount(player_money):
    while True:
        bet_amount = input("Bet Amount: ")
        if bet_amount == "x":
            return bet_amount

        bet_amount = float(bet_amount)
        if bet_amount < 5:
            print("The minimum bet is 5.")
        elif bet_amount > 1000:
            print("The maximum bet is 1000.")
        elif bet_amount > player_money:
            print("You don't have enough money.")
        else:
            print()
            return bet_amount


def play_player_hand(deck_of_cards, hand):
    while True:
        player_choice = input("Hit or Stand? (h/s): ")
        print()


def display_cards(hand, title):
    print(title.upper())
    for card in hand:
        print(deck.display_card(card))
    print()


# create a loop to be ended by the user
def play_until_exit(player_money):
    while True:
        player_bet = input("Bet Amount: ")

        deck_of_cards = deck.get_deck()
        deck.shuffle(deck_of_cards)

        dealer_hand = deck.get_empty_hand()
        player_hand = deck.get_empty_hand()

        deck.add_card(player_hand, deck.deal_card(deck_of_cards))
        deck.add_card(dealer_hand, deck.deal_card(deck_of_cards))
        deck.add_card(player_hand, deck.deal_card(deck_of_cards))

        display_cards(dealer_hand, "DEALER'S SHOW CARD:")
        display_cards(player_hand, "YOUR CARD:")

        # User exit and input validation for player's bet
        if player_bet == 'x':
            break
        elif int(player_bet) < 5:
            print("ERROR: The minimum bet is 5 part 1.")
            continue
        elif int(player_bet) > 1000:
            print("ERROR: The maximum bet is 1000.")
            continue
        elif int(player_bet) > player_money:
            print("ERROR: You don't have enough money for that bet.")
            continue
        else:
            hand_result = play_player_hand(deck_of_cards, player_hand)

        deck.add_card(dealer_hand, deck.deal_card(deck_of_cards))

        if deck.calculate_hand_points(player_hand) <= 21:
            while deck.calculate_hand_points(dealer_hand) < 17:
                deck.add_card(dealer_hand, deck_of_cards)

        display_cards(dealer_hand, "DEALER'S CARDS")

        # display points
        dealer_points = deck.calculate_hand_points(dealer_hand)
        player_points = deck.calculate_hand_points(player_hand)
        print("YOUR POINTS:   ", player_points)
        print("DEALER POINTS: ", dealer_points)

        # Possible results due to random number generator
        if player_points > 21:
            player_money = round(player_money - float(player_bet), 2)
            print("Sorry, you busted. You lose.")
        elif player_points == 21 and len(player_hand) == 2:
            if dealer_points == 21 and len(dealer_hand) == 2:
                print("Bad luck, you both got a Blackjack! Nobody wins.")
            else:
                player_money = round(player_money + (float(player_bet) * 1.5), 2)
                print("BLACKJACK!")

        elif dealer_points == 21 and len(dealer_hand) == 2:
            player_money = round(player_money - float(player_bet), 2)
            print("The dealer got a Blackjack. You lose.")
        elif dealer_points > 21:
            player_money = round(player_money + float(player_bet), 2)
            print("The dealer busted. You win!")
        elif player_points > dealer_points:
            player_money = round(player_money + float(player_bet), 2)
            print("You Won!")
        elif dealer_points > player_points:
            player_money = round(player_money - float(player_bet), 2)
            print("You Lose.")
        else:
            print("You and the dealer pushed.")

        print(f"Money: {int(player_money)}\n")


# player_money is in main() so it persists through hands
def main():
    display_header()
    player_money = int(input("Starting money:  "))




main()
