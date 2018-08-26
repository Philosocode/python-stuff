import random  # Get the 'random' MOD.
messages = [
    'Well then',  # Store the random messages.
    'Halp me',
    'So be it',
    'You die today',
    'SUPER!!!',
    'Wow',
    'You suck',
    'Let\'s go!!!',
    'Nublet'
]

# Choose a random number from List 'messages'.
# Random Integer between 0 and the length of messages (9).
print(messages[random.randint(0, len(messages) - 1)])
