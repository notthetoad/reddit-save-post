import praw
import praw.exceptions
import json

from praw.models import Submission, Comment

class User:

    def __init__(self, client_id, client_secret, username, password, user_agent):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.user_agent = username

    def login(self):
        try:
            reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            username=self.username,
            password=self.password,
            user_agent=self.user_agent
            )
        except RedditAPIException as e:
            print(e)
        return reddit

    def get_saved(self, reddit_instance):
        posts = []
        comments = []

        for item in reddit_instance.user.me().saved(limit=3):
            if isinstance(item, Submission):
                posts.insert(0, item)
            elif isinstance(item, Comment):
                comments.insert(0, item)
            else:
                pass
        return posts, comments
