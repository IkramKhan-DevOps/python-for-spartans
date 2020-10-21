def list_simple():
    """RULES

    changeable,
    indexing,
    sorted,
    duplication
    """
    #   [0  1  2  3  4  5  6  7  8]  INDEX
    v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #      [0     1    2    3    4    5 ]  + INDEX
    alex = ['x', 'e', 'p', 'a', 'o', 'l']
    #      [-6   -5   -4   -3   -2   -1 ]  - INDEX

    print("Ikram", "Khan")
    print("Ikram" + "Khan")

    print(alex[3], alex[5], alex[1], alex[0])
    print(alex[3] + alex[5] + alex[1] + alex[0])
    print(f"{alex[3]}{alex[5]}{alex[1]}{alex[0]}")

    print(v[::2])
    print(alex[:2])
    print(alex[3:])
    print(alex[1:4])

    print("LAST: ", alex[-1])

    # print(v[0])
    # print(v[8])
    # print(v[5])

    # LENGTH
    # print(len(v))
    # print()

    # CHANGE
    # print("List Before > ", v)
    # v[0] = 10
    # v[4] = 11
    # print("List After  > ", v)


def loop_list():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    for number in numbers:
        print(number)


def find_no_list():
    """ Find values in list.

        for number in numbers:
            if number == "alex":
                print("Alex Captured")
                break

                VS

        print("alex" in numbers)

    :return:
    """
    numbers = [1, "alex", 3, "tik_tok", 5, "alex", 7, 8]

    count = 0
    for number in numbers:
        if number == "alex":
            print("Alex Captured on index: ", count)
            break
        count += 1
