import os
import hashlib


class Hashing:
    def __init__(self, password, salt_size):
        self.password = password
        self.salt_size = salt_size

    def hash_salt(self, salt_size):
        salt = os.urandom(self.salt_size)
        return salt

    def hash_password(self, password):
        hashed = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), self.salt, 100_000)
        return hashed

    def stored_hash(self):
        storage = self.salt + self.hashed
        return storage
