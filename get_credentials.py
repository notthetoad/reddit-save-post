import json
import os

from getpass import getpass


def get_credentials():
    credentials = {}
    cred_file = os.path.isfile('./credentials.json')
    if cred_file:
        with open('credentials.json', 'r') as f:
            data = json.load(f)
            credentials = {**data}
    else:
        user = input('username: ')
        credentials['username'] = user
        credentials['user_agent'] = user
        credentials['password'] = getpass('password: ')
        credentials['client_id'] = input('client_id: ')
        credentials['client_secret'] = input('client_secret: ')
        save_to_file = input("Do you want to save credentials to file? [y/N]: ")
        if save_to_file.lower() == 'y':
            with open('credentials.json', 'w') as f:
                f.write(json.dumps(credentials))
        else:
            pass
    return credentials
