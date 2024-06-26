import getpass

from database import (
    addRecord,
    create_masterkey,
    fetch_masterkey,
    fetch_password,
    fetch_site_names,
    fetch_usernames,
)
from encrypt import decrypt, encrypt, hash
from fzf import FzfPrompt
from password import generate_password


def verify_masterkey(masterkey):
    e_masterkey = fetch_masterkey()  ## fetches encrypted hashed masterkey
    # print(e_masterkey)
    # if e_masterkey == []:
    #     print("You haven't created a master key")
    #     master_key = input("Enter master key: ")
    #     e_masterkey = create_masterkey(master_key)
    # print(hash(masterkey), decrypt(masterkey, e_masterkey))
    try:
        return hash(masterkey).decode() == decrypt(masterkey, e_masterkey)
    except ValueError:
        return False


def test_verify():
    print(verify_masterkey(b"rahul"))
    print(verify_masterkey(b"deepak"))


# test_verify()
if __name__ == "__main__":

    print("Checking master key")
    checker = fetch_masterkey()
    if len(checker) == 0:
        print("You haven't created a master key")
        master_key = input("Enter master key: ")
        # create_masterkey(master_key)
        if create_masterkey(master_key):
            print("Master key created")
    fzf = FzfPrompt()
    mychoice = fzf.prompt(choices=["register_new_password", "show_passwords"])
    if mychoice[0] == "register_new_password":
        # master_key = input("Enter master key: ")
        master_key = getpass.getpass(prompt="Enter master key: ")
        master_key = master_key.encode()
        if verify_masterkey(master_key):
            sitename = input("Site name: ")
            username = input("Username: ")
            choice = fzf.prompt(
                choices=["generate your own password?", "auto-generate password?"]
            )
            e_password = ""
            if choice[0] == "generate your own password?":
                password = input("Enter your password: ")

                e_password = encrypt(master_key, password)
            elif choice[0] == "auto-generate password?":
                e_password = generate_password(master_key)
            addRecord(sitename, username, e_password)
        else:
            print("Wrong master key")
            exit()
    if mychoice[0] == "show_passwords":
        sites = fetch_site_names()
        site = fzf.prompt(choices=sites)
        sitename = site[0]
        usernames = fetch_usernames(sitename)
        username = fzf.prompt(choices=usernames)
        user_name = username[0]
        e_password = fetch_password(sitename, user_name)
        e_password = e_password[0]
        # print(f"the e-password is {e_password}")
        # master_key = input("Enter master key: ")
        master_key = getpass.getpass(prompt="Enter the key: ")
        master_key = master_key.encode()
        if verify_masterkey(master_key):
            password = decrypt(master_key, e_password)
            print(password)
        else:
            print("Wrong master key")
            exit()
