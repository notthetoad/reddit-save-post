import csv
import sqlite3
from sqlite3 import Error

statements = [
    """CREATE TABLE IF NOT EXISTS post (
        post_id text PRIMARY KEY,
        title text,
        fullname text,
        subreddit text,
        url text,
        permalink text,
        selftext text
        ); """,
    """CREATE TABLE IF NOT EXISTS comment (
        comment_id text PRIMARY KEY,
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
        self.connection = sqlite3.connect(db_file)
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
            except Error:
                pass
        self.connection.commit()

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
            except Error:
                pass
        self.connection.commit()

    def export_items(self, db_name, sql):
        items = self.connection.execute(sql)
        col_title = [desc[0] for desc in items.description]
        f_name = db_name.split('.')[0]
        f_item = sql.split()
        with open(f"{f_name}_{f_item[-1]}.csv", 'w') as f:
            writer = csv.writer(f)
            writer.writerow(col_title)
            writer.writerows(items)

    def export_to_csv(self, db_name):
        self.export_items(db_name, 'SELECT * FROM post')
        self.export_items(db_name, 'SELECT * FROM comment')
