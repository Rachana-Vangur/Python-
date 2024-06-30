import getpass
import smtplib

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.ehlo()
smtp_obj.starttls()

from_email = input("from/your email: ")
password = input("your password: ")

smtp_obj.login(from_email, password)

to_email = input("to email: ")
subject = input("Subject: \n")
message = input("Message: \n")

print("This will be your mail:\n")

msg = f"From: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{message}"
print(msg)


smtp_obj.sendmail(from_email, to_email, msg)
print("Message is sent")
smtp_obj.quit()
