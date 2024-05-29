# Фільтрація списку товарів

from datetime import datetime, date, time, timedelta


dt_now = datetime.now()  # Дата на данний момент



el_dt = []
eat = ['овочі', 'молочні продукти']

with open('csv_file.csv', newline='', encoding='utf-8') as file:
    line = file.readline()
    while line:
        line.strip()
        sp = [x.strip() for x in line.split(';')]
        if sp[1] in eat:
            el_dt.append(sp)  # До цього рядка (включно) працює коректно.
#  todo:Попробувати о'єднати \23 та \25 в один +++
        #dt_x = [datetime.strptime(str(y[-1]), "%Y-%m-%d") for y in el_dt]

        # dt_str = [str(dt[-1]) for dt in el_dt]  # Видає формат list[list[str]]!!!! (todo: Зробити щоб виводився лише str) +++
        #
        # dt_obj = datetime.strptime(dt_str[-1], "%Y-%m-%d")  # Перетворення str в datetime

        #  TODO: Замінити елемент strdate на datetime в зміній el_dt
    for w in el_dt:
        for count, date_str in enumerate(w):
            w[count] = datetime.strptime(date_str, '%Y-%m-%d')


        #if dt_str in el_dt:
            #el_dt.pop(dt_str[-1]) and el_dt.append(dt_obj)

       #el_dt.pop(-1) and el_dt.append(dt_obj)
        print(el_dt)


        line = file.readline()  #  Остання стрічка коду


# todo порівняти всі змінні з поточною датою, та виписати ті товари у яких закінчується
#  строк придатності через тиждень або раніше



# todo створити файл у який запишуться результати нашої програми (артікул;категорія;назва;днів до непридатності)
# Приклад вихідного файлу:
#артікул;категорія;назва;днів до непридатності
# 005;овочі;Помідори;6
# 006;молочні продукти;Сир;3
# 009;овочі;Цибуля;0
# 018;молочні продукти;Масло;4
# 034;молочні продукти;Сир;1

