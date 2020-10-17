def student_info_args(*student):
    """ARB ARGUMENTS.

    WHY :: ?
    1#  MEANS => Random, Sequence
    """

    print('NAME     : ', student[0])
    print('FATHER   : ', student[1])
    print('CLASS    : ', student[2])
    print('ROLL     : ', student[3])
    print('STATUS   : ', student[4])
    print()


def sum_360(*numbers):
    """
    ARB ARGUMENTS.

    WHY :: ?
    1#  MEANS => Random, Sequence
    """
    result = 0
    for number in numbers:
        result = result + number
    print(result)


def student_info_kwargs(university: str, **student):
    """"
    ARB KEYWORD ARGUMENTS.

    WHY :: ?
    1#  MEANS => Random, Sequence
    2#  KEYWORDS
    """

    print('NAME     : ', student['name'])
    print('FATHER   : ', student['father'])
    print('CLASS    : ', student['class_name'])
    print('ROLL     : ', student['rollno'])
    print('STATUS   : ', student['active'])


def student_info(roll_no=0, active=False, name=None):
    """
    Default arguments.

    1#  Non-defaults >> Default args
    2#  Sequence must be followed except these two conditions
        1 >> [all-default]
        2 >> [all-non-default]
    """
    print('NAME   : ', name)
    print('ROLL   : ', roll_no)
    print('STATUS : ', active)
    print()


def student_info_key(name, roll_no, active):
    """Keyword  arguments

    print('NAME   : ', name)
    print('ROLL   : ', roll_no)
    print('STATUS : ', active)
    """

    print('NAME   : ', name)
    print('ROLL   : ', roll_no)
    print('STATUS : ', active)

