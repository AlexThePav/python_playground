
def main():
    # hashable, immutable
    the_int = 1
    print(hash(the_int))
    print(id(the_int))
    print("---")

    the_bool = True
    print(hash(the_bool))
    print(id(the_bool))
    print("---")

    the_None = None
    print(hash(the_None))
    print(id(the_None))
    print("---")

    the_tuple = (1, "")
    print(hash(the_tuple))
    print(id(hash(the_tuple)))
    print("---")

    the_string = "hi"
    print(hash(the_string))
    print(id(the_string))
    print("---")


    # unhashable, mutable
    print(hash([1, 2]))
    print(hash({1, 2}))
    print(hash({"key", 2}))
    


if __name__ == "__main__":
    main()
