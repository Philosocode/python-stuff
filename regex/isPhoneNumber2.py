def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-' or text[7] != '-':
		return False
	for i in range(4, 7):	
		if not text[i].isdecimal():
			return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True

message = input("Enter message here: \n> ")		# Get message from user.
for i in range(len(message)):	# Scan through the message, character-by-character.
	chunk = message[i:i+12]		# Taking a chunk of 12 chars at a time (this is how long a phone number is)
	# e.g. "I am a cool "	" am a cool b"	"am a cool be"	"m a cool bea"	" a cool bean"	"a cool bean."
	if isPhoneNumber(chunk):	# if isPhoneNumber returns True:
		print("Phone number found: " + chunk)

print("Done")