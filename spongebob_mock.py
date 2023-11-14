def spongemock():
    inp = input("Enter text here, and watch this software mock you\n>")
    mock=[]
    for i in inp:
        if i.index(i.index() % 2 == 0):
            i.upper()
        else:
            i.lower()
    mock.append(str("".join(i)))
    print(mock)

spongemock()
# Still have a lot to figure out about this one. Gotta make sure we fix the index part, but unsure how to proceed.
