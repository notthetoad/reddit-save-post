import sqlite3
import praw

from database import create_connection
from sql_func import create_tables
from get_credentials import get_credentials

def main():
    creds = get_credentials()
    conn = create_connection("test_db.db")
    if conn is not None:
        create_tables(conn)
    else:
        print('conn is None')

    reddit = praw.Reddit(
        client_id=creds['client_id'],
        client_secret=creds['client_secret'],
        user_agent=creds['user_agent'],
        username=creds['username'],
        password=creds['password']
    )
    print(reddit.read_only)

if __name__ == '__main__':
    main()