# Guest Name = Key, Items = Value
allGuests = {'Alice': {'apples': 5, 'pretzels': 3},
			 'Bob': {'ham sandwiches': 3, 'apples': 2},
			 'Carol': {'cups': 3, 'apple pies': 1} }

# FUNC: Count how many things the Guests brought.
def totalBought(guests, item): # guests = allGuests. Item = Values.
# NOTE: the guest names aren't used in this script.
	numBought = 0; # Set the default to 0.
	for k, v in guests.items(): # k = Key, v = Value, from allGuests.items(ONLY)
	# Update 'numBought' with the VAL from 'item'. Default to 0 if N/A.
		numBought = numBought + v.get(item, 0)
	return numBought # Return the updated numBought.

print('The number of things being brought:')
# FUNC 'totalBought' with PARAMs DICT: 'allGuests' and VAL.
print(' - Apples     ' + str(totalBought(allGuests, 'apples')))
print(' - Cups       ' + str(totalBought(allGuests, 'cups')))
print(' - Cakes      ' + str(totalBought(allGuests, 'cakes')))
print(' - Ham Sandwiches  ' + str(totalBought(allGuests, 'ham sandwiches')))
print(' - Apple Pies      ' + str(totalBought(allGuests, 'apple pies')))