#HIPPO QUICK EMAIL SERVICE v3 | Copyright Chris Vintsanis 2021
import smtplib
import getpass
import os
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


def send_email(email, password):
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		
		while True:
			try:
				smtp.login(email, password)
			except smtplib.SMTPAuthenticationError:
				second = True
				print(Fore.RED + Style.BRIGHT + "[ERROR]: Credentials are wrong, please enter them again!")
				email = str(input("Enter your Gmail address and press enter: "))
				password = str(getpass.getpass("Enter your email's password and press enter: "))
				continue
			try:
				if second == True:
					save_creds = str(input("Do you want your new info to be saved [Y/n]?: "))
					yes = ['Y', 'y', 'Yes', 'YES']
					if save_creds in yes:
						if os.path.exists('creds.txt'):
							os.remove('creds.txt')
							f = open('creds.txt', 'w+')
							f.write('s')
							f.write('\n' + email)
							f.write('\n' + password)
							f.close()
						else:
							f = open('creds.txt', 'w+')
							f.write('s')
							f.write('\n' + email)
							f.write('\n' + password)
							f.close()
					else:
						pass
				else:
					pass
			except UnboundLocalError:
				pass

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
				smtp.sendmail(email, contacts, message)
			except smtplib.SMTPRecipientsRefused:
				print(Fore.RED + Style.BRIGHT + "[ERROR]: The email address you entered is invalid, please type it again!")
				for i in range(num_of_con):
					receiver_address = str(input('Enter an email address: '))
					contacts.append(receiver_address)
				continue
			break
		print(Fore.GREEN + Style.BRIGHT + "The email has been sent!")