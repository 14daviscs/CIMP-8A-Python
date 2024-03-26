#!/usr/bin/env python3

FILENAME = "movies.txt"


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
def add_movie(movies):
    movie = input("Movie: ")
    movies.append(movie)
    write_movies(movies)
    print(f"{movie} was added.\n")


# Display movies in the list
def list_movies(movies):
    for i in range(len(movies)):
        print(f"{i}. {movies[i]}")
    print()


# Delete a movie from the list
def delete_movie(movies):
    number = int(input("Number: "))
    if number < 1 or number > len(movies):
        print("Invalid movie number.\n")
    else:
        movie = movies.pop(number - 1)
        write_movies(movies)
        print(f"{movie} was deleted.\n")


def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
    return movies


def write_movies(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(f"{movie}\n")


def main():
    # Create and initialize the movie list
    movie_list = ["Star Wars",
                  "The Empire Strikes Back",
                  "Return of the Jedi"]

    display_menu()
    movies = read_movies()  # get the movies from the file

    while True:
        command = input("Command: ").lower()
        if command == "list":
            list_movies(movie_list)
        elif command == "add":
            add_movie(movie_list)
        elif command == "del":
            delete_movie(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")


if __name__ == "__main__":
    main()
