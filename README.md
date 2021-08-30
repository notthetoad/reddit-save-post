# reddit-save-post
Python script for downloading user's saved posts and comments from reddit account.

### User credentials, if saved, are stored in json file and are not secure, be sure to not share it with anyone.

## Dependencies
> python3
> praw

## How to use it
Go to ***reddit.com*** log in and go to ***preferences***. Go to ***apps*** tab and scroll down, next press ***create app***. Get your account's

```
client_id
client_secret
username
password
```

Then go to project's directory and run `$ python main.py` in console and the program will prompt you to fill in the credentials, or run `$ python main.py -h` for help and optional arguments.

## What it does and what's it for
It takes user's credentials to get access to saved posts and comments on their reddit account. Downloads them and saves them in `sqlite3` database.
Reddit only allows to see up to 1000 saved items, consistent updating database solves this issue.
