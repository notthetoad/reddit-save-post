import praw
import json
import argparse
import sys
import os

from database import Db
from user import User

def create_arg_parse():
    parser = argparse.ArgumentParser(description="Saves posts and comments from user's reddit account.")
    parser.add_argument('-c', '--credentials', dest='credentials', metavar='[file]', required=False, help="path to file containing user credentials")
    parser.add_argument('-d', '--database', dest='database', metavar='[name]', required=False, help="choose a name for your database file")
    parser.add_argument('--export', dest='export', required=False, action='store_true', help="export database to Comma Separated Values (CSV) file")
    parser.add_argument('--format', dest='format', required=False, action='store_true', help="show format for credentials file")
    return parser

def main():
    arg_parser = create_arg_parse()
    parsed_args = arg_parser.parse_args()

    db_name = 'test.db'
    db = Db(db_name)

    if parsed_args.credentials:
        if os.path.exists(parsed_args.credentials):
            user = User(parsed_args.credentials)
            posts, comments = user.get_saved()
            db.save_posts(posts)
            db.save_comments(comments)
        else:
            print("File does not exist")

    if parsed_args.format:
        sys.stdout.write('{\n\t"username": username,\n\t"password": password,\n\t"client_id": client_id,\n\t"client_secret": client_secret\n\t"user_agent": user_agent\n}\n')
        sys.exit()

    if parsed_args.database:
        db_name = args.database + '.db'

    if parsed_args.export:
        db.export_to_csv(db_name)

if __name__ == '__main__':
    main()