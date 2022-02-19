
def func_no_args_no_return():
    num1 = 10
    num2 = 20
    print(num1+num2)


def even_odd(number=10):
    if number % 2 == 0:
        print("Number", number, "is Even")
    else:
        print("Number", number, "is Odd")


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


even_odd()
even_odd(21)
