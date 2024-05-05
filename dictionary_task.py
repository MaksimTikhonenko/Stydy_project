# Перетворення двох списків у словник

keys = ['name', 'age', 'from', 'city', 'street', 'house number']
values = ['Maksim', 24, 'Ukraine', 'Vinnitsa', 'Soborna', 5]

my_dict = dict(zip(keys, values))  # zip() - об'єднання двох списків, dict() - перетворення у словник.

print(my_dict)
