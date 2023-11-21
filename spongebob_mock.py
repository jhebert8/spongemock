def spongemock():
    inp = input("Enter text here, and watch this software mock you\n>")
    mock=[]
    for (i, char) in enumerate(inp):
        if i % 2 == 0:
            mock.append(char.upper())
        else:
            mock.append(char.lower())

    print("".join(mock))

spongemock()
