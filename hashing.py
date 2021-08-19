import os
import hashlib


class Hashing:
    def __init__(self, password, salt):
        self.password = password
        self.salt = salt

    def hash_salt(self, salt):
        
