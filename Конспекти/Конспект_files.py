# Відкриття файлу

# open(), щоб відкрити файл. Вона повертає об'єкт файлу.

file = open('filename.txt', 'mode')

# stdout - стандартний вивід / standard output
# stderr - стандартний вивід помилок / standard error
# stdin  - стандартний ввід/ standard input

# socket - файл для обміну даними по мережі <address>:<port>

#     'mode' вказує режим, в якому відкривається файл:
#         'r' - Читання (режим за замовчуванням)
#         'w' - Запис (створює новий файл або очищує існуючий файл)
#         'a' - Додавання (додає до кінця файлу)
#         'b' - Бінарний режим (використовується з іншими режимами, наприклад, 'rb' або 'wb')

# Характеристики файла:
# - шлях
# - дозволи для доступу
# - metadata (час створення, час останньої зміни)

# Windows - ім'я файлів нечутливі до регістру
# Linux, Mac - регістр має значення

# Цикл роботи з файлом:
# - open: 
    # - відкрити і створити якщо не існує
    # - відкрити тільки якщо існує
    # - створити навіть якщо вже існує і переписати поверху
# - read() or write()
# - flush()
# - close()

# Читання файлу
#   read(): Читає весь файл
#   readline(): Читає одну строку за раз
#   readlines(): Читає всі строки у список

file = open('filename.txt', 'r')
content = file.read()
file.close()

# Використання readline()

# Створення файлу з декількома строками
with open('example.txt', 'w') as file:
    file.write('Перша строка\n')
    file.write('Друга строка\n')
    file.write('Третя строка\n')

# Читання файлу по одній строкі за раз
with open('example.txt', 'r') as input_file:
    line = input_file.readline()
    while line:
        print(line.strip())  # метод strip() видаляє пробіли на початку і в кінці строки
        line = input_file.readline()

# Використання readlines()

# Створення файлу з декількома строками
with open('example.txt', 'w') as file:
    file.write('Перша строка\n')
    file.write('Друга строка\n')
    file.write('Третя строка\n')

# Читання всіх строк файлу в список
with open('example.txt', 'r') as file:
    lines = file.readlines()

# Виведення кожної строки зі списку
for line in lines:
    print(line.strip())  # метод strip() видаляє пробіли на початку і в кінці строки

# Запис у файл
# write()
# writelines()

file = open('filename.txt', 'w')
file.write('Hello, world!')
file.close()

# Оператор with автоматично закриває файл

with open('filename.txt', 'r') as file:
    content = file.read()


# читання та запис текстових файлів

# Запис у файл
with open('example.txt', 'w') as file:
    file.write('This is an example.')

# Читання з файлу
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
