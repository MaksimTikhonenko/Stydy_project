# Фільтрація словника за типом значень

my_dict = {'name': 'Maksim', 'age': 24, 'from': 'Ukraine', 'city': 'Vinnitsa', 'street': 'Soborna', 'house number': 5}

int_my_dict = [values for values in my_dict.values() if isinstance(values, int)]

print(int_my_dict)
