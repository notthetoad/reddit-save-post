import sqlite3
from sqlite3 import Error

create_post_table = """CREATE TABLE IF NOT EXISTS post (
                        id integer PRIMARY KEY,
                        post_id integer UNIQUE,
                        title text,
                        fullname text,
                        subreddit text,
                        url text,
                        permalink text,
                        selftext text
                        ); """

create_comment_table = """CREATE TABLE IF NOT EXISTS comment (
                            id integer PRIMARY KEY,
                            comment_id integer UNIQUE,
                            body text,
                            permalink text,
                            score integer
                            );"""


insert_post = """INSERT INTO post (
                        post_id,
                        title,
                        fullname,
                        subreddit,
                        url,
                        permalink,
                        selftext)
                    VALUES (?, ?, ?, ?, ?, ?, ?);"""


insert_comment = """INSERT INTO comment (
                        comment_id,
                        body,
                        permalink,
                        score)
                    VALUES (?, ?, ?, ?);"""

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

def save_posts(conn, posts):
    c = conn.cursor()
    for post in posts:
        try:
            values = (
                post.id,
                post.title,
                post.fullname,
                post.subreddit.display_name,
                post.url,
                post.permalink,
                post.selftext
            )
            c.execute(insert_post, values)
        except Error:
            c.execute("SELECT count(*) FROM post WHERE post_id = ?", (values[0], ))
    conn.commit()

def save_comments(conn, comments):
    c = conn.cursor()
    for comm in comments:
        try:
            values = (
                comm.id,
                comm.body,
                comm.permalink,
                comm.score
            )
            c.execute(insert_comment, values)
        except Error:
            c.execute("SELECT count(*) FROM post WHERE post_id = ?", (values[0], ))
    conn.commit()