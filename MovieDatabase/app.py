import datetime
import psycopg2
from SQL_Pyhton_Projects.MovieDatabase.database import create_tables, add_movie, get_movies, watch_movie, get_watched_movies, add_user, search_movies



menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies
3) View all movies
4) Watch a movie
5) View watched movies
6) Add user
7) Search movie
8) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
create_tables()


def prompt_add_movie():
    movie_title = input('Movie title: ')
    movie_release_date = input("Release date (dd-mm-YYYY): ")
    parse_date = datetime.datetime.strptime(movie_release_date, "%d-%m-%Y").timestamp()
    return movie_title, parse_date


def prompt_watched_movies():
    username = input("Please input the username: ")
    movies = get_watched_movies(username)
    if movies:
        print_movies_list("Watched", movies)
    else:
        print("That user has watched no movies yet!")


def prompt_watch_movie():
    movie_id = input("Enter the movie id of the movie you watched: ")
    username = input("Enter your username: ")
    return username, movie_id


def prompt_add_user():
    username = input("Please input the new user: ")
    add_user(username=username)

def prompt_search_movie():
    key_word = input('Please enter a keyword: ')
    movies = search_movies(key_word)
    if movies:
        print_movies_list('Found', movies)
    else:
        print('No movies found')


def print_movies_list(heading, movies):
    print(f" --- {heading} movies -- ")
    for movie in movies:
        movie_release_date = datetime.datetime.fromtimestamp(movie[2])
        human_date = movie_release_date.strftime('%b %d %Y')
        print(f"{movie[0]}: {movie[1]}: {human_date}")


user_input = input(menu)

while user_input != "8":
    if user_input == "1":
        title, release_date = prompt_add_movie()
        add_movie(title = title, release_timestamp = release_date)
    elif user_input == "2":
        movies = get_movies(True)
        print_movies_list("UPCOMING", movies)
    elif user_input == "3":
        movies = get_movies()
        print_movies_list("ALL", movies)
    elif user_input == "4":
        username, movie_id = prompt_watch_movie()
        watch_movie(username=username, movie_id=movie_id)
    elif user_input == "5":
        prompt_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == '7':
        prompt_search_movie()
    else:
        print("Invalid input, please try again!")
    user_input = input(menu)