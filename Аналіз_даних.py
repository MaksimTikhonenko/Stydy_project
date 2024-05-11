# Задача: Аналіз даних про книги

list_dct = [{'author': 'Tolkien', 'book': 'The Hobbit', 'pages_count': 310},
            {'author': 'Orwell', 'book': '1984', 'pages_count': 328},
            {'author': 'Tolkien', 'book': 'The Lord of the Rings', 'pages_count': 1178},
            {'author': 'Orwell', 'book': 'Animal Farm', 'pages_count': 112}] # Список словників, кожен словник містить 3 ключа і 3 значення
result = {} # Словник що містить ключ = 1 значення (ім'я автора) : кортеж (2 значення, 3 значення)

a = list_dct[0]  # Розбиваю список на різні словники, щоб працювати з кожним словником окремо
b = list_dct[1]
c = list_dct[2]
d = list_dct[3]

#TODO

for i in a.items():

    print(i)

for k, v in a:
    if k == 'author':
        new_a = {v: ()}
        if k == 'book':
            new_a[v] = v
        if k == 'pages_count':
            new_a[v] = v
print(new_a)



#result = {...} #todo Перебираю список словнік, витягую лише ті словники у яких максимальне значення сторінок у книзі
