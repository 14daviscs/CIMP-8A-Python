#!/usr/bin/env python3

import random

max_number = 9


def start_message():
    print("Guess the number!\n")


def number_game():
    rand_int = random.randint(1, max_number)
    attempts = 0
    print(f"I'm thinking of a number from 1 to {max_number}\n")
    while True:
        guess = int(input("Your guess: "))
        if guess == rand_int:
            attempts += 1
            print(f"You guessed it in {attempts} tries.\n")
            break
        elif guess < rand_int:
            attempts += 1
            print("Too low.")
        elif guess > rand_int:
            attempts += 1
            print("Too high.")


def main():
    start_message()
    restart = "y"
    while restart == "y":
        number_game()
        restart = input("Play again? (y/n): ")
        print()
    print("Bye!")


main()
