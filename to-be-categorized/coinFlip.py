import random
heads = 0
# i goes from 1 to 1000... 1000 coin flips.
for i in range(1, 1001):
    # here, 1 is heads. 0 is tails.
    if random.randint(0, 1) == 1:
        heads = heads + 1
    # we're done 500 flips.
    if i == 500:
        print("Halfway done")
print("Heads came up " + str(heads) + ' times.')
