import re

def stripper(str):
	stripRe = re.compile(r'(\s*)(\w*)(\s*)')
	mo = stripRe.search(str)
	return mo.group(2)

stripped = stripper(input("Enter a string:\n> "))
print("Here is your stripped string: \"" + stripped + "\"")