import re

th_re = re.compile(r'''(
	Alice | Bob | Carol
	\s
	eats | pets | throws
	\s
	apples | cats | baseballs
	\.
	)''', re.VERBOSE | re.I)

three_re = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.I)
mo = three_re.search("Bob eats cats.")
mo.group()