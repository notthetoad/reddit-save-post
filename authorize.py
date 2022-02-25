import json
import os

from getpass import getpass

class Credentials:

    def __init__(self, user_info):
        self.user_info = {}

    def get_user_credentials(self):
        self.user_info['username'] = input('username: ')
        self.user_info['password'] = getpass('password: ')
        self.user_info['client_id'] = input('client_id: ')
        self.user_info['client_secret'] = input('client_secret: ')
        self.user_info['user_agent'] = input('user_agent: ')
