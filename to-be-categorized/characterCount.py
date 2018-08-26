import pprint
message = "It was a bright and sunny day. We were riding on the train to G."
count = {} # The count will be stored in a DICT named 'count'.

# This FOR-Loop will go through each CHAR in 'message'.
for character in message:
	# Hmm... so setting the default for each character (I, w, a) to 0.
	count.setdefault(character, 0)
	# If the character is encountered again, +1
	count[character] = count[character] + 1

pprint.pprint(count)