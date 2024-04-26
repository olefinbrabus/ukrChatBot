import os
import hashlib
import hmac


def generate_salt():
    return os.urandom(32)


def generate_key(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)


password = input("Enter the password: ")
salt = generate_salt()
key = generate_key(password, salt)

new_key = input("Enter the new key: ")
new_key_hashed = generate_key(new_key, salt)

if hmac.compare_digest(new_key_hashed, key):
    print('Password match!')
else:
    print('Password incorrect!')