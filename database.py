import sqlite3
from sqlite3 import Error

statements = [
    """CREATE TABLE IF NOT EXISTS post (
        id integer,
        post_id integer PRIMARY KEY,
        title text,
        fullname text,
        subreddit text,
        url text,
        permalink text,
        selftext text
        ); """,
    """CREATE TABLE IF NOT EXISTS comment (
        id integer,
        comment_id integer PRIMARY KEY,
        body text,
        permalink text,
        score integer
        );"""
]

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

class Db:
    
    def __init__(self, db_file):
        self.connection = sqlite3.connection(db_file)
        cursor = self.connection.cursor()
        for stmt in statements:
            cursor.execute(stmt)

    def save_posts(self, posts):
        cursor = self.connection.cursor()
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
                cursor.execute(insert_post, values)
            except:
                pass
        cursor.commit()

    def save_comments(self, comments):
        cursor = self.connection.cursor()
        for comm in comments:
            try:
                values = (
                    comm.id,
                    comm.body,
                    comm.permalink,
                    comm.score
                )
                cursor.execute(insert_comment, values)
            except:
                pass
        cursor.commit()
