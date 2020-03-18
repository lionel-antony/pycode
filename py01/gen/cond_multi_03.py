gpa = float(input('What was your GPA? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= 0.85 and lowest_grade >= 0.70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print('You made the Honour Roll!!!')
else:
    print('You are a Dumbo!!!')