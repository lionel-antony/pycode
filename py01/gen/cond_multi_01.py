country = input('What country do you live in? ')
if country == 'Canada':
    province = input('What province do you live in? ')
tax = 0

# if province == 'Alberta':
#     tax = 0.05
# elif province == 'Nunavut':
#     tax = 0.10
# elif province == 'Ontario':
#     tax = 0.15
# else:
#     tax = 0.25

if country == 'Canada':
   if province in ('Alberta', 'Yukon', 'Vancouver'):
       tax = 0.05
   elif province == 'Nunavut':
       tax = 0.10
   elif province == 'Ontario':
       tax = 0.15
   else:
       tax = 0.25
else:
    tax = 0


print(tax)
