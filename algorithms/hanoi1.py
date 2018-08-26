def hanoi(disc, source="Peg 1", dest="Peg 3", spare="Peg 2"):
    if disc > 0:
        # Move n-1 discs from source to spare (left to center)
        # Move discs 1 and 2 to spare
        hanoi(disc - 1, source, spare, dest)

        # Move the bottom disc to destination
        print("Move disc %d from %s to %s" % (disc, source, dest))

        # Move n-1 discs from spare to destination
        # Move discs 1 and 2 to destination
        hanoi(disc - 1, spare, dest, source)


if __name__ == "__main__":
    hanoi(int(input("How many discs?\n> ")))
