from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

MAX_PASSWORD_LEN = 64


def hash(key):
    hash_obj = SHA256.new(key)
    digest = hash_obj.digest()
    digest = digest.hex()

    key = digest[:32]
    key = key.encode()

    return key


def test_hash():
    key = b"rahul"
    key = hash(key)
    print(key)
    print(len(key))


def make_blocks(s):

    p1 = s[:16]
    p2 = s[16:32]
    p3 = s[32:48]
    p4 = s[48:]

    return [p1, p2, p3, p4]


def encrypt(master_key, password):
    password = password.encode()
    master_key = hash(master_key)
    cipher = AES.new(master_key, AES.MODE_ECB)
    password = pad(password, MAX_PASSWORD_LEN)
    blocks = make_blocks(password)
    e_password = ""
    for block in blocks:
        e_password += cipher.encrypt(block).hex()
    return e_password


def decrypt(master_key, epassword):

    master_key = hash(master_key)
    cipher = AES.new(master_key, AES.MODE_ECB)
    epassword = bytes.fromhex(epassword)
    password = ""
    blocks = make_blocks(epassword)
    for block in blocks:
        password += cipher.decrypt(block).hex()
    password = bytes.fromhex(password)
    # print(password)
    try:
        password = unpad(password, MAX_PASSWORD_LEN)
    except ValueError:
        return ""
    password = password.decode()

    return password


def test_encrypt():
    e_text = encrypt(b"rahul", b"deepak:")
    print(e_text)
    password = decrypt(b"rahul", e_text)
    print(password)


# test_encrypt()
