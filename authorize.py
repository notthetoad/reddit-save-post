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
        save = input("Do you wish to save credentials to file? [y/N]: ")
        if save == 'y':
            name = input("Please enter file name: ")
            if name != None:
                self.save_credentials_to_file(name)
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

    def save_credentials_to_file(self, f_name):
        with open(f"{f_name}.json", 'w') as fp:
            json.dump(self.user_info, fp)
        print("saved to file")


