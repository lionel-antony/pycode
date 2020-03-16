def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('enter your first name: ')
first_name_initial = get_initial(first_name, True)

print('Your initial is: ' + first_name_initial)