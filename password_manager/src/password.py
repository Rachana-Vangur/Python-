import random
import string

from database import fetch_masterkey
from encrypt import decrypt, encrypt, hash


def verify_masterkey(masterkey):
    e_masterkey = fetch_masterkey()  ## fetches encrypted hashed masterkey
    # print(hash(masterkey), decrypt(masterkey, e_masterkey))
    try:
        return hash(masterkey).decode() == decrypt(masterkey, e_masterkey)
    except ValueError:
        return False


def generate_password(master_key):

    password = ""
    # passwords are mostly 16 chars long
    length = 16
    char_pool = string.ascii_letters + string.punctuation + string.digits
    while length != len(password):
        password += random.choice(char_pool)
    e_password = encrypt(master_key, password)
    return e_password


def check_password(password):

    min_len, max_len = 8, 64
    count = 0
    if min_len <= len(password) <= max_len:
        for letter in password:
            if letter.isupper() or letter.islower():
                count += 1
            if letter.isascii():
                count += 1
            if letter in password.punctuation:
                count += 1
            if letter.isdigit():
                count += 1
        if count >= 4:
            return True
        else:
            print("Password is either missing punctuations or digits")

    return False
