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
        player_choice = input("Hit or Stand (h/s): ")
        print()

        if player_choice.lower() == "h":
            deck.add_card(hand, deck.deal_card(deck_of_cards))
            display_cards(hand, "YOUR CARDS:")
            if deck.calculate_hand_points(hand) > 21:
                break
        elif player_choice.lower() == "s":
            break
        else:
            print("not a valid choice, please try again.")

    return hand


def display_cards(hand, title):
    print(title.upper())
    for card in hand:
        print(deck.display_card(card))
    print()


def display_outcome(player_points, player_hand, dealer_points, dealer_hand, bet_amount, player_money):
    if player_points > 21:
        print("Sorry, you busted. You lose.")
        player_money -= bet_amount
    elif player_points == 21 and len(player_hand) == 2:
        if dealer_points == 21 and len(dealer_hand) == 2:
            print("Bad luck, you both got a Blackjack! Nobody wins.")
        else:
            print("BLACKJACK!")
            player_money += bet_amount * 1.5
    elif dealer_points == 21 and len(dealer_hand) == 2:
        print("The dealer got a Blackjack. You lose.")
        player_money -= bet_amount
    elif dealer_points > 21:
        print("The dealer busted. You win!")
        player_money += bet_amount
    elif player_points > dealer_points:
        print("You Won!")
        player_money += bet_amount
    elif dealer_points > player_points:
        print("You Lose.")
        player_money -= bet_amount
    else:
        print("You and the dealer pushed.")

    return player_money


# player_money is in main() so it persists through hands
def main():
    display_header()
    player_money = get_starting_amount()

    while True:
        bet_amount = get_bet_amount(player_money)

        if bet_amount == "x":
            break

        bet_amount = float(bet_amount)

        deck_of_cards = deck.get_deck()
        deck.shuffle(deck_of_cards)

        dealer_hand = deck.get_empty_hand()
        player_hand = deck.get_empty_hand()

        deck.add_card(player_hand, deck.deal_card(deck_of_cards))
        deck.add_card(dealer_hand, deck.deal_card(deck_of_cards))
        deck.add_card(player_hand, deck.deal_card(deck_of_cards))

        display_cards(dealer_hand, "DEALER'S SHOW CARD:")
        display_cards(player_hand, "YOUR CARD:")

        player_hand = play_player_hand(deck_of_cards, player_hand)

        deck.add_card(dealer_hand, deck.deal_card(deck_of_cards))
        if deck.calculate_hand_points(player_hand) <= 21:
            while deck.calculate_hand_points(dealer_hand) < 17:
                deck.add_card(dealer_hand, deck.deal_card(deck_of_cards))

        display_cards(dealer_hand, "DEALER'S CARDS")

        dealer_points = deck.calculate_hand_points(dealer_hand)
        player_points = deck.calculate_hand_points(player_hand)
        print("YOUR POINTS:   ", player_points)
        print("DEALER POINTS: ", dealer_points)

        player_money = display_outcome(player_points, player_hand, dealer_points, dealer_hand, bet_amount, player_money)

        print("Money:", round(player_money, 2))
        print()

        if player_money < 5:
            print("You are out of money.")
            break

        play_again = input("Play again? (y/n): ")

        if play_again.lower() != "y":
            print("Come back soon.")
            break

    print("Bye")


main()
