chris = {}
chris['first'] = 'Chris'
chris['last'] = 'Harris'

susan = {}
susan['first'] = 'Susan'
susan['last'] = 'Ibach'

people = []
people.append(chris)
people.append(susan)
people.append({
    'first': 'Bill', 'last': 'Gates'
})

print(people)
