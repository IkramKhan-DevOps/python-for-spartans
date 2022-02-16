
def func_if():
    number1 = 1
    number2 = 2
    if number2 == number1:
        print("Same")


def func_if_else():
    number1 = 1
    number2 = 2
    if number2 == number1:
        print("Same")
    else:
        print("Not Same")


def func_if_elif_else():
    number1 = 1
    number2 = 2
    if number2 > number1:
        print("Number2")
    elif number1 > number2:
        print("Number1")
    else:
        print("Same")


def calculate_marks():
    number = int(input("Enter your marks   : "))

    if number >= 90:
        print("Excellant")
    elif number >= 80 and number < 90:
        print("Very Good")
    elif number >= 60 and number < 80:
        print("Good")
    else:
        print("Fail")


def authentication():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "admin":
        print("Welcome: ", username)
    else:
        print("Failed to Login! Wrong credentials")


# func_if()
# func_if_else()
# func_if_elif_else()
# calculate_marks()
authentication()
