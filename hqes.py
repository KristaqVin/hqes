# HIPPO QUICK EMAIL SERVICE v3 | Copyright 2021 Chris Vintsanis
import os
import colorama
import getpass
from colorama import Fore, Style
colorama.init(autoreset=True)

print(Fore.BLUE + Style.BRIGHT + "Welcome to Hippo Quick Email Service v3!\n")

try:
	f = open('creds.txt')
	cont = f.read().splitlines()
	if 's' in cont:
		email_address = cont[1]
		email_password = cont[2]
	else:
		print(Fore.RED + Style.BRIGHT + "[ERROR]: Code 01, please report this!")
		exit()
except FileNotFoundError:
	email_address = str(input("Enter your Gmail address and press enter: "))
	email_password = str(getpass.getpass("Enter your email's password and press enter: "))
	save_credentials = str(input("Do you want your credentials to be saved [Y/n]?: "))
	yes = ['Y', 'y', 'YES', 'yes', 'Yes']
	if save_credentials in yes:
		with open('creds.txt', 'w+') as f:
			f.write('s')
			f.write('\n' + email_address)
			f.write('\n' + email_password)
	else:
		pass

print(Fore.CYAN + "1. Send an email")
print(Fore.CYAN + "2. Read email")
print(Fore.CYAN + "3. Exit the script")
print(Fore.CYAN + "4. Delete your credentials\n")


while True:
	action = str(input(''))
	if action == '1':
		import send_email as s
		s.send_email(email=email_address, password=email_password)
	elif action == '2':
		import read_email as r
		r.read_email(email_a=email_address, password=email_password)
	elif action == '3':
		print(Fore.RED + Style.BRIGHT + "Goodbye, :)")
		exit()
	elif action == '4':
		if os.path.exists("creds.txt"):
			os.remove('creds.txt')
			print(Fore.GREEN + Style.BRIGHT + "Credentials succesfuly deleted!")
			exit()
		else:
			print(Fore.RED + Style.BRIGHT + "[ERROR]: No saved credentials were found!")
			exit()
	else:
		print(Fore.RED + "[ERROR]: Invalid option!")
		continue
