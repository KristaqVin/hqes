#HIPPO QUICK EMAIL SERVICE v2.3 | Copyright Chris Vintsanis 2021
import imaplib
import email
from email.header import decode_header
import getpass
import os
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

username = str(input("Enter your Gmail address and press enter: "))
password = str(getpass.getpass("Enter your email's password and press enter: "))


def read_email():
    global username
    global password
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    while True:
        try:
            imap.login(username, password)
        except:
            print(Fore.RED + Style.BRIGHT + "[ERROR]: Credentials are wrong, enter them again!")
            username = str(input("Enter your Gmail address and press enter: "))
            password = str(getpass.getpass("Enter your email's password and press enter: "))
            continue
        break

    status, messages = imap.select("INBOX")
    N = 3
    messages = int(messages[0])

    for i in range(messages, messages-N, -1):
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding)
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                print("Subject:", subject)
                print("From:", From)
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            print(body)
                        elif "attachment" in content_disposition:
                            pass
    					
                else:
                    content_type = msg.get_content_type()
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        print(body)
                if content_type == "text/html":
                    pass

                print("="*100)
    imap.close()
    imap.logout()