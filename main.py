import praw
import json

from praw.models import Submission, Comment
from getpass import getpass
from database import Db
from user import User
from authorize import Authorize

def get_saved(reddit):
    posts = []
    comments = []

    for item in reddit.user.me().saved(limit=None):
        if isinstance(item, Submission):
            posts.insert(0, item)
        elif isinstance(item, Comment):
            comments.insert(0, item)
        else:
            pass
    return posts, comments

def main():
    db = Db('reddit_saved.db')
    auth = Authorize()
    user_credentials = auth.get_user_credentials()
    user = User(**user_credentials)
    posts, comments = get_saved(user.login())

    db.save_posts(posts)
    db.save_comments(comments)

if __name__ == '__main__':
    main()