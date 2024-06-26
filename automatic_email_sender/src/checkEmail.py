import imaplib

imap_obj = imaplib.IMAP4_SSL("imap.gmail.com")

email = input("email: ")
password = input("password: ")

imap_obj.login(email, password)
options = imap_obj.list()
options = options[1]
for opt in options:
    print(opt)

print(imap_obj.select("inbox"))
