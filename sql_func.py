import sqlite3
from sqlite3 import Error

# TODO
create_post_table = """ CREATE TABLE IF NOT EXISTS post (
                        id integer PRIMARY KEY,
                        post_id integer,
                        title text,
                        url text,
                        permalink text,
                        subreddit text,
                        date text
                        ); """

create_comment_table = """ CREATE TABLE IF NOT EXISTS comment (
                            id integer PRIMARY KEY,
                            body text,
                            score integer
                            );"""
statements = [
    create_post_table,
    create_comment_table,
]

def create_tables(conn):
    try:
        c = conn.cursor()
        for s in statements:
            c.execute(s)
    except Error as e:
        print(e)