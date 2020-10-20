def func_for():
    """For Loop Range.

    range(limit)              -> limit : exclude
    range(start, limit)       -> start: include, limit : exclude
    range(start, limit)       -> start: include, limit : exclude
    range(start, limit, gap)  -> start: include, limit : exclude, gap
    """

    # [print(x) for x in range(1, 10, 2)]
    print("__EVENS__")
    for c in range(0, 21, 2):
        print(c)


def func_while():
    """Increment in While.

    i += 1      SUCCESSFUL
    i = i + 1   SUCCESSFUL
    i++         FAILED
    """

    i = 1
    while i < 6:
        print("Rohail Loop: ", i)
        i += 1


def sum_100():
    """Logic Sum of 100 numbers.

        sum = 0
        for i in range(1, 101):
            sum = sum + i
        print("SUM: ", sum)
    """
    print(sum(range(1, 101)))


def is_prime(number):
    """Prime Number Logic.

    rule: number/1 , number/number
    :param number:
    :return:

    1 number/1      remove => 2
    2 number/number remove => number
    """
    for i in range(2, number):

        if number % i == 0:
            print("NOT-Prime")
            break
    else:
        print("PRIME")


def anila():
    number = int(input("Enter no: "))
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print("Sheraz")
