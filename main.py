import sqlite3
import praw
import json

from praw.models import Submission, Comment
from getpass import getpass
from database import Db
from user import User

def get_user_credentials():
    user_credentials = {}
    user_credentials['username'] = input("Username: ")
    user_credentials['password'] = getpass("Password: ")
    user_credentials['client_id'] = input("Client_id: ")
    user_credentials['client_secret'] = input("Client_secret: ")
    user_credentials['user_agent'] = user_credentials['username']
    save_to_file = input("Do you want to save credentials to json file? [y/N]: ")
    if save_to_file.lower() == 'y':
        with open('credentials.json', 'w') as f:
            f.write(json.dumps(user_credentials))
    else:
        pass
    return user_credentials

def main():
    user_credentials = get_user_credentials()
    reddit_user = User(**user_credentials)


if __name__ == '__main__':
    main()