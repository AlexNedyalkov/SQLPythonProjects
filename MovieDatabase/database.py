import os
import psycopg2
import datetime

from dotenv import load_dotenv

load_dotenv()

CREATE_MOVIE_TABLE = """CREATE TABLE if not exists movies (
                   id SERIAL PRIMARY KEY,
                   title TEXT,
                    release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE if not exists users (
                    username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE if not exists watched (
                            user_username TEXT,
                            movie_id INTEGER,
                            FOREIGN KEY (user_username) references users(username),
                            FOREIGN KEY (movie_id) references movies(id)
);"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES(%s, %s);"
INSERT_USER = "INSERT INTO users (username) VALUES (%s)"
INSERT_USER = "INSERT INTO users (username) VALUES (%s)"
DELETE_MOVIE = "DELETE FROM movies WHERE title = %s;"
SELECT_ALL_MOVIES = "SELECT * FROM movies"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > %s;"
SELECT_WATCHED_MOVIES = """SELECT * FROM movies
 JOIN watched on watched.movie_id = movies.id 
 JOIN users on users.username = watched.user_username 
 WHERE username =  %s;"""
SEARCH_MOVIE = """SELECT * FROM movies WHERE title LIKE %s;"""
INSERT_WATCHED_MOVIES = "INSERT INTO watched (user_username, movie_id) VALUES(%s, %s);"
SET_MOVIES_WATCHED = "UPDATE movies SET watched=1 WHERE title = %s;"

# os.environ gives us a dictionary of environment variables currently defined. We're accessing the DATABASE_URL
# variable in there, which should give us the correct value if we loaded the .env file correctly.
connection = psycopg2.connect(os.environ["DATABASE_URL"])


def create_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_MOVIE_TABLE)
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(CREATE_WATCHED_TABLE)


def add_user(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_USER, (username,))


def add_movie(title, release_timestamp):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(upcoming = False):
    with connection:
        with connection.cursor() as cursor:
            if upcoming:
                today_timestamp = datetime.datetime.today().timestamp()
                cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
            else:
                cursor.execute(SELECT_ALL_MOVIES)
            return cursor.fetchall()


def watch_movie(username, movie_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WATCHED_MOVIES, (username, movie_id))


def get_watched_movies(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_WATCHED_MOVIES, (username,))
            return cursor.fetchall()


def search_movies(key_word):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SEARCH_MOVIE, ('%' + key_word + '%',))
            return cursor.fetchall()