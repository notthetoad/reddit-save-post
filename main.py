import sqlite3
import praw

from praw.models import Submission, Comment
from database import create_connection
from sql_func import create_tables, save_posts, save_comments
from get_credentials import get_credentials

def init_reddit(credentials):
    creds = get_credentials()

    reddit = praw.Reddit(
        client_id=creds['client_id'],
        client_secret=creds['client_secret'],
        user_agent=creds['user_agent'],
        username=creds['username'],
        password=creds['password']
    )
    return reddit

def get_saved(reddit):
    posts = []
    comments = []
    for item in reddit.user.me().saved(limit=None):
        if isinstance(item, Submission):
            posts.append(item)
        elif isinstance(item, Comment):
            comments.append(item)
        else:
            pass
    return posts, comments

def main():
    creds = get_credentials()
    conn = create_connection("reddit_saved.db")
    if conn is not None:
        create_tables(conn)
    else:
        print('Could not create database tables.')
    
    posts, comments = get_saved(init_reddit(get_credentials))
    save_posts(conn, posts)
    save_comments(conn, comments)

    conn.close()

if __name__ == '__main__':
    main()