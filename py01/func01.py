from datetime import datetime


def print_time(msg):
    print(msg)
    print(datetime.now())
    print()


first_name = 'susan'
print_time('task 1 completed')

for x in range(0, 10):
    print(x)

print_time('task 2 completed')
