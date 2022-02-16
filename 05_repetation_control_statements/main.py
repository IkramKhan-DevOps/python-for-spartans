

def even_or_odd():
    print("______ODD________")
    for x in range(1, 21, 2):
        print(x)

    print("______EVEN________")
    for x in range(2, 21, 2):
        print(x)


def print_a_table():
    table = int(input("Enter Table: "))
    range_ = int(input("Enter Range: "))

    for value in range(1, range_, 1):
        print(table, "*", value, "=", table * value)


value = None                 # INIT
while value != 'stop':         # CONDITION
    value = input("Enter your name: ")





