# reddit-save-post
Python script for downloading user's saved posts and comments from reddit account.

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

Then go to project's directory and run `$ python3 main.py` in console and the program will prompt you to fill in the credentials.

## What it does and what's it for
It takes user's credentials to get access to saved posts and comments on their reddit account. Downloads them and saves them in `sqlite3` database.
Reddit only allows to see up to 1000 saved items, consistent updating database solves this issue.
