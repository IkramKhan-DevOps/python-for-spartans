def if_only(name1, name2):
    if name1 == name2:
        print("Both are Equal")


def if_else_only(name1, name2):
    if name1 == name2:
        print("Both are Equal")
    else:
        print("Both are Not Equal")


def check_grade(marks):
    if marks > 75:
        print("A")
    elif marks > 50:
        print("B")
    elif marks > 25:
        print("C")
    else:
        print("D")


def short_if(name1, name2):
    if name1 == name2 : print("EQUAL")


def short_if_else(name1, name2):
    # result_if > if condition > else > result_else
    print("Both are Equal") if name1 == name2 else print("Both are Not Equal")


def short_if_elif_else():
    """Short if elif else -- Or - ternary
        if a > b:
            print("A")
        else:
            if a == b:
                print("==")
            else:
                print("B")
    """
    a = 102
    b = 104

    print("A") if a > b else print("==") if a == b else print("B")


def logical_operators():
    """Logical Op.

    AND = and = &&
    OR  = or  = ||
    """
    a = 10
    b = 20
    c = 10

    if a == c or c < b:
        print("OKAY")
    else:
        print("FAIL")
