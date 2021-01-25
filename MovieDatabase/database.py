import sqlite3
import datetime

CREATE_MOVIE_TABLE = """CREATE TABLE if not exists movies (
                   id INTEGER PRIMARY KEY,
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

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES(?, ?);"
INSERT_USER = "INSERT INTO users (username) VALUES (?)"
INSERT_USER = "INSERT INTO users (username) VALUES (?)"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = """SELECT * FROM movies
 JOIN watched on watched.movie_id = movies.id 
 JOIN users on users.username = watched.user_username 
 WHERE username =  ?;"""
SEARCH_MOVIE = """SELECT * FROM movies WHERE title LIKE ?;"""
INSERT_WATCHED_MOVIES = "INSERT INTO watched (user_username, movie_id) VALUES(?, ?);"
SET_MOVIES_WATCHED = "UPDATE movies SET watched=1 WHERE title = ?;"


connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIE_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)


def add_user(username):
    with connection:
        connection.execute(INSERT_USER, (username,))


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(upcoming = False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def watch_movie(username, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIES, (username, movie_id))


def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()


def search_movies(key_word):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIE, ('%' + key_word + '%',))
        return cursor.fetchall()