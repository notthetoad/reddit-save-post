import praw
import json

from getpass import getpass
from database import Db
from user import User
from authorize import Authorize

def main():
    db = Db('reddit_saved.db')
    auth = Authorize()
    user_credentials = auth.get_user_credentials()
    user = User(**user_credentials)
    posts, comments = user.get_saved(user.login())

    db.save_posts(posts)
    db.save_comments(comments)

if __name__ == '__main__':
    main()