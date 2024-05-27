# Фільтрація списку товарів

from datetime import datetime


dt_now = datetime.now()  # Дата на данний момент



el_datetime = []
eat = ['овочі', 'молочні продукти']

with open('csv_file.csv', newline='', encoding='utf-8') as file:
    line = file.readline()
    while line:
        line.strip()
        sp = [x.strip() for x in line.split(';')]
        if sp[1] in eat:
            el_datetime.append(sp)

        line = file.readline()






# todo порівняти всі змінні з поточною датою, та виписати ті товари у яких закінчується
#  строк придатності через тиждень або раніше
# todo створити файл у який запишуться результати нашої програми
