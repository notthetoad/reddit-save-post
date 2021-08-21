import praw
import json

from praw.models import Submission, Comment
from getpass import getpass
from database import Db
from user import User
from authorize import Authorize

def main():
    db = Db('test_class.db')
    auth = Authorize()
    user_credentials = auth.get_user_credentials()
    user = User(**user_credentials)
    reddit_user = user.login()
    saved = reddit_user.user.me().saved(limit=5)

    posts = [p for p in saved if type(p) == Submission]
    comments = [c for c in saved if type(c) == Comment]

    db.save_posts(posts)
    db.save_comments(comments)

if __name__ == '__main__':
    main()