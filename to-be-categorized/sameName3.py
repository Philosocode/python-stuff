def spam():
	global eggs
	eggs = 'spam global'

def bacon():
	eggs = 'bacon in bacon()'

def ham():
	print('eggs in ham()')

eggs = 42 # This is global
spam()
print(eggs)