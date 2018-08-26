def isPhoneNumber(text):
	if len(text) != 12:	# Check the STR Length: 12 characters.
		return False
	for i in range(0, 3):	# Check the first 3 digits.
		if not text[i].isdecimal():	# If these are not 'decimals' / numbers, return Falses
			return False
	if text[3] != '-' or text[7] != '-': # If the 4th character or the 8th character are not -, return False
		return False
	for i in range(4, 7):	
		if not text[i].isdecimal():
			return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True	# If it passes all checks, return True

text = input("I am a phone number checker. Enter your text here: \n> ")
print(isPhoneNumber(text))