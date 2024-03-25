#!/usr/bin/env python3


# Display the menu
def display_menu():
    print("The Movie List program\n")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a new movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()


# Add a new movie
def add(movie_list):
    movie = input("Movie: ")
    movie_list.append(movie)
    print(f"{movie} was added.\n")


# Display movies in the list
def list_movies(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print(f"{i}. {movie}")
    print()


# Delete a movie from the list
def delete(movie_list):
    number = int(input("Movie Number: "))

    # Test for valid movie number
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie} was deleted.\n")


def main():
    # Create and initialize the movie list
    movie_list = ["Star Wars",
                  "The Empire Strikes Back",
                  "Return of the Jedi"]

    display_menu()

    while True:
        command = input("Command: ").lower()
        if command == "list":
            list_movies(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")


if __name__ == "__main__":
    main()
