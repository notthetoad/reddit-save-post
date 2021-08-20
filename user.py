import praw
import praw.exceptions
import json

from hashlib import sha256

# TODO make get_user_credentials function that gives User class credentials to login on initialization in main.py when refactoring to OOP
class User:

    def __init__(self, client_id, client_secret, username, password, user_agent):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.user_agent = username
        self.hash_password(password)

    def login(self):
        try:
            reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            username=self.username,
            password=self.hash_password(self.password),
            user_agent=self.user_agent
            )
        except RedditAPIException as e:
            print(e)
        return reddit

    def hash_password(self, password):
        return sha256(self.password.encode('utf-8')).hexdigest()

    def read_json(self, file_name = None):
        credentials = {}
        if file_name:
            with open(f'./{file_name}') as f:
                credentials = json.load(f)
        else:
            credentials = {
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'username': self.username,
                'password': self.hash_password(self.password),
                'user_agent': self.user_agent
            }
        return credentials

# c_dict = {"username": "nyko_LoL", "user_agent": "nyko_LoL", "password": "ChangeForTesting", "client_id": "Iffb_La7YJ6MeFkMsOyIUw", "client_secret": "kFxuSs8RaKwFKjqw9KhAxgcXeF9ENA"}
