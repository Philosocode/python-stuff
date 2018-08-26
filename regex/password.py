import re

# Test that the password is at least 8 characters long.
charRegex = re.compile(r'\w{8, 20}')
# Test that the password has at least one upper & lower char.
minRegex = re.compile(r'[A-Z]+[a-z]+\d+')

# Get the password.
password = input("Input a password\n>>> ")

# Test the password
if charRegex.search(password) and minRegex.search(password):
	print("Your password stronk.")
else:
	print("Work on the password.")