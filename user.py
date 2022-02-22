import praw
import praw.exceptions
import json

from praw.models import Submission, Comment

class User:

    def __init__(self, file):
        self.file = file
        self.user_data = self.authorize()
        self.r_instance = self.login()

    def authorize(self):
        with open(self.file) as f:
            data = json.load(f)
            return {**data}

    def login(self):
        try:
            reddit = praw.Reddit(
                client_id=self.user_data['client_id'],
                client_secret=self.user_data['client_secret'],
                username=self.user_data['username'],
                password=self.user_data['password'],
                user_agent=self.user_data['user_agent']
            )
        except RedditAPIException as error:
            print(error)
        return reddit

    def get_saved(self):
        posts = []
        comments = []

        for item in self.r_instance.user.me().saved(limit=None):
            if isinstance(item, Submission):
                posts.insert(0, item)
            elif isinstance(item, Comment):
                comments.insert(0, item)
            else:
                pass
        return posts, comments
