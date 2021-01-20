import datetime
from SQL_Pyhton_Projects.MovieDatabase.database import create_tables, add_movie, get_movies, watch_movie, get_watched_movies

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
create_tables()


def prompt_add_movie():
    movie_title = input('Movie title: ')
    movie_release_date = input("Release date (dd-mm-YYYY): ")
    parse_date = datetime.datetime.strptime(movie_release_date, "%d-%m-%Y").timestamp()
    return movie_title, parse_date

def prompt_watch_movie():
    watched_title = input("Enter the movie title you have watched: ")
    username = input("Enter your username: ")
    return username, watched_title

def print_movies_list(heading, movies):
    print(f" --- {heading} movies -- ")
    for movie in movies:
        movie_release_date = datetime.datetime.fromtimestamp(movie['release_timestamp'])
        human_date = movie_release_date.strftime('%b %d %Y')
        print(f"{movie['title']}: {human_date}")

def print_watched_movies(username, movies):
    print(f" --- {username} watched movies ---")
    for movie in movies:
        print(f"{movie['title']}")


user_input = input(menu)

while user_input != "6":
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
        username, title = prompt_watch_movie()
        watch_movie(username, title)
    elif user_input == "5":
        username = input("Please input the username: ")
        movies = get_watched_movies(username)
        print_watched_movies(username, movies)
    else:
        print("Invalid input, please try again!")
    user_input = input(menu)