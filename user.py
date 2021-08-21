import praw
import praw.exceptions
import json

from hashlib import sha256

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
