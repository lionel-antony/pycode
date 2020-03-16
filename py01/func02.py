def get_initial(name):
    initial = name[0:1]
    return initial


fn = input('enter fn: ')
fni = get_initial(fn)

mn = input('enter mn: ')
mni = get_initial(mn)

ln = input('enter ln: ')
lni = get_initial(ln)

print('your initials are: ' + fni + mni + lni)
