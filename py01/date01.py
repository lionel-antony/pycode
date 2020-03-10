# from datetime import datetime
# current_date = datetime.now()
# print('Today is: ' + str(current_date))

# from datetime import datetime, timedelta
# today = datetime.now()
# one_day = timedelta(days=1)
# yesterday = today - one_day
# print('Yesterday was: ' + str(yesterday))
# one_week = timedelta(weeks=1)
# last_week = today - one_week
# print('Last week was: ' + str(last_week))

# from datetime import datetime, timedelta
# today = datetime.now()
# print('Date: ' + str(today))
# print('Day: ' + str(today.day))
# print('Month: ' + str(today.month))
# print('Year: ' + str(today.year))
# print('Hour: ' + str(today.hour))
# print('Minute: ' + str(today.minute))
# print('Second: ' + str(today.second))
# print('MicroSecond: ' + str(today.microsecond))

from datetime import datetime, timedelta
birthday = input('When is your birthday (dd/mm/yyyy) ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print