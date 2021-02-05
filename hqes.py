# HIPPO QUICK EMAIL SERVICE v2.2 | Copyright 2021 Chris Vintsanis

import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

print(Fore.BLUE + Style.BRIGHT + "Welcome to Hippo Quick Email Service v2.1!")
print(Fore.CYAN + "1. Send an email")
print(Fore.CYAN + "2. Read email")
print(Fore.CYAN + "3. Exit the script\n")

while True:
	action = str(input(''))
	if action == '1':
		import send_email
	elif action == '2':
		import read_email
	elif action == '3':
		exit()
	else:
		print(Fore.RED + "[ERROR]: Invalid option!")
		continue
