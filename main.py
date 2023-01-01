import smtplib
from email.message import EmailMessage
from faker import Faker
import re

fake = Faker("tr_TR") # if you need change lang

CUSTOMERS = []

MAIN_MAIL = ""

COUNT = 0

# CREATE MAILS (TR LANGUAGE)

for i in range(100):
    # GMAIL

    fmail = fake.email()

    FIND_1 = re.search("@example.com", fmail)
    FIND_2 = re.search("@example.net", fmail)
    FIND_3 = re.search("@example.org", fmail)


    if FIND_1:
        RECEVIER = re.sub("@example.com", "", fmail)
    elif FIND_2:
        RECEVIER = re.sub("@example.net", "", fmail)
    elif FIND_3:
        RECEVIER = re.sub("@example.org", "", fmail)

    CUSTOMERS.append(RECEVIER+"@gmail.com")

for i in range(100):
    # HOTMAIL

    fmail = fake.email()

    FIND_1 = re.search("@example.com", fmail)
    FIND_2 = re.search("@example.net", fmail)
    FIND_3 = re.search("@example.org", fmail)


    if FIND_1:
        RECEVIER = re.sub("@example.com", "", fmail)
    elif FIND_2:
        RECEVIER = re.sub("@example.net", "", fmail)
    elif FIND_3:
        RECEVIER = re.sub("@example.org", "", fmail)

    CUSTOMERS.append(RECEVIER+"@hotmail.com")

for i in range(100):
    # OUTLOOK

    fmail = fake.email()

    FIND_1 = re.search("@example.com", fmail)
    FIND_2 = re.search("@example.net", fmail)
    FIND_3 = re.search("@example.org", fmail)


    if FIND_1:
        RECEVIER = re.sub("@example.com", "", fmail)
    elif FIND_2:
        RECEVIER = re.sub("@example.net", "", fmail)
    elif FIND_3:
        RECEVIER = re.sub("@example.org", "", fmail)

    CUSTOMERS.append(RECEVIER+"@outlook.com")

for i in range(100):
    # PROTON MAIL

    fmail = fake.email()

    FIND_1 = re.search("@example.com", fmail)
    FIND_2 = re.search("@example.net", fmail)
    FIND_3 = re.search("@example.org", fmail)


    if FIND_1:
        RECEVIER = re.sub("@example.com", "", fmail)
    elif FIND_2:
        RECEVIER = re.sub("@example.net", "", fmail)
    elif FIND_3:
        RECEVIER = re.sub("@example.org", "", fmail)

    CUSTOMERS.append(RECEVIER+"@protonmail.com")

for i in range(100):
    # YAHOO

    fmail = fake.email()

    FIND_1 = re.search("@example.com", fmail)
    FIND_2 = re.search("@example.net", fmail)
    FIND_3 = re.search("@example.org", fmail)


    if FIND_1:
        RECEVIER = re.sub("@example.com", "", fmail)
    elif FIND_2:
        RECEVIER = re.sub("@example.net", "", fmail)
    elif FIND_3:
        RECEVIER = re.sub("@example.org", "", fmail)

    CUSTOMERS.append(RECEVIER+"@yahoo.com.com")


while COUNT <= len(CUSTOMERS):

    try:
        msg = EmailMessage()
        msg.set_content("Message")
        msg['Subject'] = 'Subject'
        msg['From'] = MAIN_MAIL
        msg['To'] = CUSTOMERS[COUNT]
        server = smtplib.SMTP_SSL('server', 465) # SERVER INFORMATION
        server.login(MAIN_MAIL, "PASSWORD") # E MAIL LOGIN
        server.send_message(msg)
        server.quit()
        
        print(f"MAIL SENDED : {CUSTOMERS[COUNT]}")

        COUNT += 1
    except IndexError:
        print("END!")
        break
