import praw
import json

from getpass import getpass
from database import Db
from user import User
from authorize import Authorize

def main():

    parser = argparse.ArgumentParser(description="Saves posts and comments from user's reddit account.")
    parser.add_argument('-c', '--credentials', dest='credentials', metavar='[file]', required=False, help="json file name with credentials e.g. \"credentials.json\"")
    parser.add_argument('-d', '--database', dest='database', metavar='[name]', required=False, help="choose a name for your database file")
    parser.add_argument('--export', dest='export', required=False, action='store_false', help="export database to Comma Separated Values (CSV) file")
    # parser.add_argument('--format', dest='format', required=False, action='store_false', help="show format for credentials file")
    args = parser.parse_args()

    # if args.format:
    #     sys.stdout.write('{\n\t"username": username,\n\t"password": password,\n\t"client_id": client_id,\n\t"client_secret": client_secret\n\t"user_agent": user_agent\n}\n')
    #     sys.exit()

    auth = Authorize()
    user_credentials = {}
    if args.credentials:
        with open(args.credentials, 'r') as f:
            data = json.load(f)
            user_credentials = {**data}
    else:
        user_credentials = auth.get_user_credentials()

    db_name = 'reddit_saved.db'
    if args.database:
        db_name = args.database + '.db'

    db = Db(db_name)
    if args.export:
        db.export_to_csv(db_name)

    user = User(**user_credentials)
    posts, comments = user.get_saved(user.login())

    db.save_posts(posts)
    db.save_comments(comments)

if __name__ == '__main__':
    main()