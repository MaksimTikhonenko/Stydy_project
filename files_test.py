from datetime import date, timedelta

with open('example.txt', 'w') as file:
    file.write('Сергій;2006-05-01\n')
    file.write('Іван;2005-05-01\n')

# text_read = ''

# with open('example.txt') as input_file:
#     text_read = input_file.read()
#     # text_readlines = input_file.readlines()
#     pass

students = []
with open('example.txt') as input_file:
    i = 1
    ln = input_file.readline()
    while ln:
        data = ln.strip().split(';')
        
        students.append({
            'name': data[1],
            'dob': date.fromisoformat(data[2])
        })

        ln = input_file.readline()

result = [s for s in students if s.dob + timedelta(days=360*14) < date.today()]

# text_readlines = None
# with open('example.txt') as input_file:
#     text_readlines = input_file.readlines()

# pass