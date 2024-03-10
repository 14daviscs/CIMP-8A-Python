#!/usr/bin/env python3

# Add constants to help make the code more readable
MOVIE_TITLE = 0
YEAR = 1
RATING = 2

movies = [["Deadpool", "2016", "1.0"],
          ["Casino Royale", "2006", "8.1"],
          ["Star Wars", "1977", "8.6"]]

movie = ["Monsters, Inc.", "2001", "8.1"]

movies.append(movie)

# We can sort on any field
# Here we will sort on the movie title
movies.sort(key=lambda x: x[MOVIE_TITLE])

# The first number is the row
# The second number of the column
print(f"Item in movies position [0][MOVIE_TITLE]: {movies[0][MOVIE_TITLE]}")
print(f"Item in movies position [3][RATING]: {movies[3][RATING]}")
print()

# Display all elements in the movies list
# We will need to use a nested for loop for this
# The first loop goes through the row
for movie in movies:
    # the second loop goes through the columns
    for item in movie:
        print(item, end=" | ")
    print()
