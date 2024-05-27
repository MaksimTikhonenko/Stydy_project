# def is_float(val):
#     try:
#         float(val)
#         return True
#     except ValueError:
#         return False
#
#
# with open('input.txt', 'r') as file:
#     lines = file.readlines()
#
# for line in lines:
#     new_line = line.strip()
#     print(is_float(new_line))

import csv
from datetime import datetime

# Ваш CSV-файл
csv_file_path = 'csv_file.csv'

# Функція для перевірки, чи є рядок об'єктом типу datetime
def is_datetime(string):
    try:
        datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

# Перевірка CSV-файлу
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Пропускаємо заголовок (якщо він є)

    for row in reader:
        for value in row:
            if is_datetime(value):
                print(f"Рядок містить об'єкт типу datetime: {value}")
                break
        else:
            continue
        break
    else:
        print("Рядків з об'єктами типу datetime не знайдено.")
