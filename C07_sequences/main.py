
# INIT
#          [0,        1,       2]
teachers = ["Zahida", "Sajil", "Shahzad"]
print(teachers)

# APPEND()
teachers.append("Sheraz")
print(teachers)

# INSERT()
teachers.insert(1, "Junaid")
print(teachers)
print()
# EXTEND
# ......
# ---------------------------------------------------------

# SLICING
#           [ 0    1    2    3    4    5    6    7 ]
#           [-8   -7   -6   -5   -4   -3   -2   -1 ]
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("TOTAL LENGTH:", len(alphabets))
print(alphabets[6])
print(alphabets[-3])
print(alphabets[0], alphabets[1], alphabets[2], alphabets[3])
print(alphabets[:4])
print(alphabets[4:])
print(alphabets[2:5])
print(alphabets[-6:-1])
print(alphabets[1:-6])

# IN
print('z' in alphabets)
if 'z' in alphabets:
    print("Not Exists")
else:
    print("Exists")

print()
# ---------------------------------------------------------------------
# LOOP OVER

for x in alphabets:
    print(x)

print()
# ---------------------------------------------------------------------
# CHANGE

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(alphabets)

alphabets[0] = 'z'
alphabets[1] = 'y'
alphabets[2] = 'x'

print(alphabets)
print()
# ---------------------------------------------------------------------
# DELETE

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
alphabets.remove('c')
alphabets.pop()
alphabets.pop(1)
del alphabets[0]

print(alphabets)
alphabets.clear()
print(alphabets)

print()
# --------------------------------------------------------------------
# METHODS
alphabets = ['z', 'x', 'y', 'd', 'g', 'f', 'e', 'h']
print(alphabets)

# SORT (2 Way)
alphabets.sort()
print(alphabets)
alphabets.sort(reverse=True)
print(alphabets)

# COPY()
alphabets2 = alphabets.copy()
print("COPIED:", alphabets2)

alphabets2 = list(alphabets)
print("COPIED:", alphabets2)

alphabets2 = alphabets
print("COPIED:", alphabets2)