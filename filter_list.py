#   Фільтрація списку товарів

from datetime import datetime

el_dt = []
eat = ['овочі', 'молочні продукти']
result_filter = []

dt_now = datetime.today()  # Дата на данний момент

with open('csv_file.csv', newline='', encoding='utf-8') as file:
    line = file.readline()
    while line:
        line.strip()
        sp = [x.strip() for x in line.split(';')]
        if sp[1] in eat:
            el_dt.append(sp)  # До цього рядка (включно) працює коректно.
        line = file.readline()  # Остання стрічка коду

#   Перетворення str в datetime, різниця в даті, запис продуктів у яких закінчується термін придатності через 7д
for w in el_dt:
    dt = datetime.strptime(w[-1], '%Y-%m-%d')
    delta = [(dt - dt_now)]
    for q in delta:
        if q.days <= 7 and q.days > 0:
            out_line = f"{w[0]};{w[1]};{w[2]};{q.days};"
            result_filter.append(out_line)

#   Cтвореня файлу та запис результату нашої програми (артікул;категорія;назва;днів до непридатності)
with open('result_filter.csv', 'w', encoding='utf-8') as file:
    for i in result_filter:
        file.writelines(i + "\n")

print("Список продуктів у яких закінчується термін придатності через 7 днів або раніше: " + "\n"
      + str(result_filter) + "\n\n" + "Цей результат записаний у файл: 'result_filter.csv'")
