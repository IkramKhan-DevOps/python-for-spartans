
if __name__ == '__main__':

    '''VARIABLES INITIALIZATION'''
    no = 10221
    name = 'Taimour'
    marks = 101.6
    active = True

    ''' NO:00 NAME:** MARKS:** ACTIVE:**  '''
    print('METHOD 1 >>>  NO:'+str(no)+' NAME:'+str(name)+' MARKS:'+str(marks)+' ACTIVE:'+str(active))
    print('METHOD 2 >>>  NO:{} NAME:{} MARKS:{} ACTIVE:{}'.format(no, name, marks, active))
    print(f'METHOD 3 >>>  NO:{no} NAME:{name} MARKS:{marks} ACTIVE:{active}')
    print()

    print(type(marks))
    print(abs(marks))
    print(round(marks))
