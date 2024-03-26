#!/usr/bin/env python3

import csv

FILENAME = "movies.csv"


# Display the menu
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("find - Find a movie")
    print("add  - Add a new movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()


# Add a new movie
def add_movie(movie_list):
    name = input("name")
    year = input("Year: ")
    movie = (name, year)
    movie_list.append(movie)
    write_movies(movie_list)
    print(f"{movie[0]} was added.\n")


# Display movies in the list
def list_movies(movie_list):
    # Test to see if there are movies in the list
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie[0]} ({movie[1]})")
        print()


# Delete a movie from the list
def delete_movie(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        write_movies(movie_list)
        print(f"{movie[0]} was deleted.\n")


def find(movie_list):
    title = input("Enter a movie title: ")
    found = False
    for movie in movie_list:
        if movie[0].lower() == title.lower():
            print(f"{movie[0]} was released in {movie[1]} and has an IMDB rating of {movie[2]}.\n")
            found = True
            break

    if not found:
        print(f"{title} was not found.\n")


def read_movies():
    movie_list = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            movie_list.append(row)
    return movie_list


def write_movies(movie_list):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movie_list)


def main():
    # Create and initialize the movie list
    movie_list = read_movies()

    display_menu()

    while True:
        command = input("Command: ").lower()
        if command == "list":
            list_movies(movie_list)
        elif command == "add":
            add_movie(movie_list)
        elif command == "del":
            delete_movie(movie_list)
        elif command == "find":
            find(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")


if __name__ == "__main__":
    main()
