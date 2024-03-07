if __name__ == "__main__":
    a = 5
    b = a
    a = 6
    print(b)

    list_a = [1]
    list_b = list_a
    list_a.append(2)
    print(list_b)

    dict_a = {"one": 1}
    dict_b = dict_a
    dict_a["two"] = 2
    print(dict_b)
