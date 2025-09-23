
def main():
    # hashable, immutable
    print("ints")
    the_int = 1
    print(hash(the_int))
    print(id(the_int))
    the_int = 2
    print(hash(the_int))
    print(id(the_int))
    print("---")

    print("bool")
    the_bool = True
    the_other_bool = True
    print(hash(the_bool))
    print(id(the_bool))
    print(hash(the_other_bool))
    print(id(the_other_bool))
    print(the_bool > the_other_bool)
    print("---")

    print("None")
    the_None = None
    print(hash(the_None))
    print(id(the_None))
    print("---")

    print("Tuple")
    the_tuple = (1, "")
    print(hash(the_tuple))
    print(id(hash(the_tuple)))
    print("---")

    print("string")
    the_string = "hi"
    the_other_string = "hi"
    print(hash(the_string), hash(the_other_string))
    print(id(the_string), id(the_other_string))
    print("---")


    # unhashable, mutable
    print(hash([1, 2]))
    print(hash({1, 2}))
    print(hash({"key", 2}))
    


if __name__ == "__main__":
    main()
