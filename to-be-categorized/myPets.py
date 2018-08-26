myPets = ['Zombie', 'JoeJoe', 'Fat-tail']
print("Enter a pet name: ")
name = input()

if name not in myPets:
	print(f"You don't have a pet named {name}.")
else:
	print(name + "is your pet.")