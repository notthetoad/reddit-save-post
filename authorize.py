import json
import os

from getpass import getpass

class UserCredentials:

    def __init__(self):
        self.user_info = {}

    def get_user_credentials(self):
        self.user_info['username'] = input('username: ')
        self.user_info['password'] = getpass('password: ')
        self.user_info['client_id'] = input('client_id: ')
        self.user_info['client_secret'] = input('client_secret: ')
        self.user_info['user_agent'] = input('user_agent: ')
        return self.user_info

    def get_user_cred_from_file(self, file):
        with open(file) as f:
            data = json.load(f)
            self.user_info = {**data}
        return self.user_info
    
    def get_credentials(self, file='credentials.json'):
        if os.path.exists(file):
            self.get_user_cred_from_file(file)
        else:
            self.get_user_credentials()
        return self.user_info
