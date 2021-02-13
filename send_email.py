#HIPPO QUICK EMAIL SERVICE v2.3 | Copyright Chris Vintsanis 2021
import smtplib
import getpass
import os
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

sender_email = str(input("Enter your Gmail address and press enter: "))
email_password = str(getpass.getpass("Enter your email's password and press enter: "))

def send_email():
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		
		global sender_email
		global email_password

		while True:
			try:
				smtp.login(sender_email, email_password)
			except smtplib.SMTPAuthenticationError:
				print(Fore.RED + Style.BRIGHT + "[ERROR]: Credentials are wrong, please type them again!")
				sender_email = str(input("Enter your gmail address and press enter: "))
				email_password = str(getpass.getpass("Enter your email's password and press enter: "))
				continue
			break

		connected = True

		subject = str(input("Type the email's subject: "))
		body = str(input("Type the email's body: "))

		message = f'Subject: {subject}\n\n{body}'

		contacts = []
		while True:
			try:
				num_of_con = int(input('Type the number of contacts: '))
				while True:
					if num_of_con == 0:
						print(Fore.RED + Style.BRIGHT + '[ERROR]: Invalid option!')
						num_of_con = int(input('Type the number of contacts: '))
						continue
					break
			except:
				print(Fore.RED + Style.BRIGHT + '[ERROR]: Value must be number!')
				continue
			break

		for i in range(num_of_con):
			receiver_address = str(input('Enter an email address: '))
			contacts.append(receiver_address)

		while True:
			try:
				smtp.sendmail(sender_email, contacts, message)
			except smtplib.SMTPRecipientsRefused:
				print(Fore.RED + Style.BRIGHT + "[ERROR]: The email address you entered is invalid, please type it again!")
				for i in range(num_of_con):
					receiver_address = str(input('Enter an email address: '))
					contacts.append(receiver_address)
				continue
			break
		print(Fore.GREEN + Style.BRIGHT + "The email has been sent!")