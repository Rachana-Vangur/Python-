import sqlite3

from encrypt import encrypt, hash

connection = sqlite3.connect("passwords.db")
print("Connected to the database")
cur = connection.cursor()


def remove_waste(lister):
    ans = []
    for i in lister:
        ans.append(i[0])
    return ans


def fetch_masterkey():
    Nothing = "~"
    command = f"""select epassword from passwords where sitename="{Nothing}" and username="{Nothing}" """
    cur.execute(command)
    master_key = cur.fetchall()
    if master_key == []:
        print("It is empty")
        return master_key
    return master_key[0][0]


def fetch_site_names():
    ##return list
    command = """select sitename from passwords"""
    cur.execute(command)
    sites = cur.fetchall()
    sites = remove_waste(sites)

    return sites


def fetch_usernames(site):
    ##return list
    command = f"""select username from passwords where sitename="{site}" """
    cur.execute(command)
    usernames = cur.fetchall()
    usernames = remove_waste(usernames)
    return usernames


def fetch_password(site, username):
    command = f"""select epassword from passwords where sitename="{site}" and username="{username}" """
    cur.execute(command)
    e_password = cur.fetchall()
    e_password = remove_waste(e_password)
    return e_password
    pass


def addRecord(sitename, username, e_password):
    command = f"""insert into passwords(sitename, username, epassword) values("{sitename}", "{username}", "{e_password}") """

    cur.execute(command)
    cur.connection.commit()

    print("Successfully added")


def create_masterkey(master_key):

    master_key = master_key.encode()
    hashed = hash(master_key)
    e_masterkey = encrypt(master_key, hashed)
    Nothing = "~"
    addRecord(Nothing, Nothing, e_masterkey)
    # return e_masterkey
    return True
