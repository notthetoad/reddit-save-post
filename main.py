import argparse
import sys

from database import Db
from user import User
from authorize import UserCredentials

def parse_arguments():
    parser = argparse.ArgumentParser(description="Saves posts and comments from user's reddit account.")
    parser.add_argument('-c', '--credentials', dest='credentials', metavar='[file]', required=False, help="file containing user credentials")
    parser.add_argument('-d', '--database', dest='database', metavar='[name]', required=False, help="choose a name for your database file")
    parser.add_argument('--export', dest='export', required=False, action='store_true', help="export database to Comma Separated Values (CSV) file")
    parser.add_argument('--format', dest='format', required=False, action='store_true', help="show format for credentials file")
    return parser.parse_args()

def main():
    parsed_args = parse_arguments()

    db_name = 'test.db'
    db = Db(db_name)
    
    user = User();
    if parsed_args.credentials:
        user.get_user_cred_from_file(parsed_args.credentials)
    else:
        user.get_user_credentials()
    posts, comments = user.get_saved()
    db.save_posts(posts)
    db.save_comments(comments)

    if parsed_args.format:
        sys.stdout.write('{\n\t"username": username,\n\t"password": password,\n\t"client_id": client_id,\n\t"client_secret": client_secret\n\t"user_agent": user_agent\n}\n')
        sys.exit()

    if parsed_args.database:
        db_name = parsed_args.database + '.db'

    if parsed_args.export:
        db.export_to_csv(db_name)

if __name__ == '__main__':
    main()
