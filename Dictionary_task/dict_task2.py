# Фільтрація словника за типом значень

my_dict = {'name': 'Maksim', 'age': 24, 'from': 'Ukraine', 'city': 'Vinnitsa', 'street': 'Soborna', 'house number': 5.5}

int_my_dict = {k: v for k, v in my_dict.items() if isinstance(v, int) or isinstance(v, float) or isinstance(v, complex)}

print(int_my_dict)
