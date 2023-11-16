mock = input("type something here and watch this piece of software mock you:\n>")

for i in mock:
    if i.index(i) % 2 == 0:
        print(i.upper())
    elif i.index(i) % 2 != 0:
        print(i.lower())
    print("".join(i))

# Still have a lot to figure out about this one. Gotta make sure we fix the index part, but unsure how to proceed.
# Don't forget to make a function out of it so it can be used by other memers
