
if __name__ == "__main__":
    # GOOD
    givenlist = ["hello", "this", "this", "is", "this", "BTechGeeks", "this", "python"]
    key = "this"
    givenlist = [element for element in givenlist if element != key]

    givenlist = ["hello", "this", "this", "is", "this", "BTechGeeks", "this", "python"]
    givenlist = list(filter(lambda element: element != key, givenlist))

    givenlist = ["hello", "this", "this", "is", "this", "BTechGeeks", "this", "python"]
    for element in list(givenlist):
        if element == key:
            givenlist.remove(element)
    print(givenlist)

    # BAD
    givenlist = ["hello", "this", "this", "is", "this", "BTechGeeks", "this", "python"]
    for element in givenlist:
        if element == key:
            givenlist.remove(element)

    
    givenlist = ["hello", "this", "this", "is", "this", "BTechGeeks", "this", "python"]
    for i, element in enumerate(givenlist):
        if element == key:
            givenlist.remove(givenlist[i])
    
    givenlist = ["hello", "this", "this", "is", "this", "BTechGeeks", "this", "python"]
    copylist = sorted(givenlist.copy(), reverse=False)
    for i, element in enumerate(copylist):
        if element == key:
            copylist.remove(copylist[i])
    print(copylist)

