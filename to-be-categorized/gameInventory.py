#! /usr/bin/env python3.

# Player Inventory is stored in a DICT.
inventory = {'sword': 1, 'health potions': 10, 'zeny': 500, 'arrow': 55 }

# FUNC: 'displayINventory' that takes 'inventory'
def displayInventory(inventory):
	print('Inventory:')
	item_total = 0 # Reset the total items.
	for k, v in inventory.items(): # For KEYs and VALs in the DICT's items.
		print(str(v) + ' ' + k) # PRINT: VAL + space + item name
		item_total += v # Add the VAL (quantity) to item_total
	print('Total number of items: ' + str(item_total))

displayInventory(inventory)