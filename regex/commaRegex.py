import re

# commaRegex = re.compile(r'\d{1,3}(\,\d\d\d)*')
commaRegex = re.compile(r"^\d{1,3}(\,\d{3})*$")

mo = commaRegex.search("42")
print(mo.group())

mo = commaRegex.search("1,234")
print(mo.group())

mo = commaRegex.search("6,368,745")
print(mo.group())

mo = commaRegex.search("12,34,567")
if mo:
	print(mo.group())

mo = commaRegex.search("1234")
if mo:
	print(mo.group())