from functions.advance_functions import \
    sum_360, student_info_kwargs

print("DOCU => ", sum_360.__doc__)
print("ANNO => ", sum_360.__annotations__)
print("DATA => ", sum_360(1, 2, 3, 4, 5))
