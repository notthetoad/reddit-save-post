import praw
import json
import argparse

from getpass import getpass
from database import Db
from user import User
from authorize import Authorize

def main():
    parser = argparse.ArgumentParser(description="Saves posts and comments from user's reddit account.")
    parser.add_argument('-c', '--credentials', dest='credentials', required=False)
    args = parser.parse_args()

    user_credentials = {}

    if args.credentials:
        with open(args.credentials, 'r') as f:
            data = json.load(f)
            user_credentials = {**data}


    db = Db('test.db')
    auth = Authorize()
    # user_credentials = auth.get_user_credentials()
    user = User(**user_credentials)
    posts, comments = user.get_saved(user.login())

    db.save_posts(posts)
    db.save_comments(comments)

if __name__ == '__main__':
    main()