import json
import os

from getpass import getpass

class Authorize:
    def __init__(self):
        self.get_user_credentials()

    def check_for_credentials(self):
        credentials_file = os.path.isfile('./credentials.json')
        if credentials_file:
            with open('credentials.json', 'r') as f:
                data = json.load(f)
                credentials_from_file = {**data}
        else:
            pass
        return credentials_from_file

    def get_user_credentials(self):
        user_credentials = self.check_for_credentials()
        if len(user_credentials.items()) > 4:
            return user_credentials
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